import os
import sys

# Vercel pysqlite3 override for ChromaDB SQLite compatibility
try:
    import pysqlite3
    sys.modules['sqlite3'] = pysqlite3
except Exception:
    pass

import asyncio
import threading
import json
import time
import base64
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request, Response, Depends, Cookie, Header, APIRouter, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, EmailStr
SentenceTransformer = None
from dotenv import load_dotenv
import hashlib

import db
from rag_engine import RAGEngine, QueryUnderstandingEngine, clean_latex_artifacts
from universal_file_reader import extract_file_content

# Fix Windows console UTF-8 output encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load Environment Variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH, override=True)

IS_VERCEL = bool(os.getenv("VERCEL"))
LOCAL_DB_PATH = "/tmp/ghl_chroma_db" if IS_VERCEL else os.path.join(BASE_DIR, "ghl_chroma_db")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@xortlogix.com").strip().lower()

def ensure_chroma_db_on_vercel():
    if IS_VERCEL and not os.path.exists(LOCAL_DB_PATH):
        src_db = os.path.join(BASE_DIR, "ghl_chroma_db")
        if os.path.exists(src_db):
            import shutil
            try:
                print("📦 [Vercel] Copying ChromaDB to /tmp on demand...")
                shutil.copytree(src_db, LOCAL_DB_PATH)
                print("✅ [Vercel] ChromaDB copied to /tmp.")
            except Exception as e:
                print(f"Copying ChromaDB to /tmp failed: {e}")

class GeminiKeyPool:
    """
    Intelligent Multi-Key Polling & Automatic Failover Engine.
    - Rotates keys round-robin (polling) to distribute token consumption across all keys.
    - Detects 429 (ResourceExhausted / RateLimit), 503 spikes, or quota exhaustion.
    - Temporarily puts exhausted key into cooldown and immediately shifts to the next healthy key.
    - Automatically recovers keys when cooldown period ends.
    """
    def __init__(self):
        self.lock = threading.Lock()
        self.index = 0
        self.keys = []
        self.key_stats = {}
        self.reload_keys()

    def reload_keys(self):
        with self.lock:
            all_keys = []
            # Read from environment
            env_keys_str = os.getenv("GEMINI_API_KEYS", "") or os.getenv("GEMINI_API_KEY", "")
            if env_keys_str:
                for k in env_keys_str.replace(";", ",").split(","):
                    k = k.strip()
                    if k and k != "YOUR_GEMINI_API_KEY_HERE" and k not in all_keys:
                        all_keys.append(k)

            # Read from .env
            if os.path.exists(ENV_PATH):
                try:
                    with open(ENV_PATH, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if line.startswith("#"):
                                continue
                            if line.startswith("GEMINI_API_KEYS=") or line.startswith("GEMINI_API_KEY="):
                                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                                for k in val.replace(";", ",").split(","):
                                    k = k.strip()
                                    if k and k != "YOUR_GEMINI_API_KEY_HERE" and k not in all_keys:
                                        all_keys.append(k)
                except Exception:
                    pass

            self.keys = all_keys
            for k in self.keys:
                if k not in self.key_stats:
                    self.key_stats[k] = {
                        "requests": 0,
                        "errors": 0,
                        "tokens_estimated": 0,
                        "cooldown_until": 0,
                        "status": "active"
                    }

    def get_candidate_keys(self, override_key: str = "") -> list:
        with self.lock:
            if not self.keys:
                self.reload_keys()

            now = time.time()
            if override_key and override_key != "YOUR_GEMINI_API_KEY_HERE":
                return [override_key] + [k for k in self.keys if k != override_key]

            if not self.keys:
                return []

            n = len(self.keys)
            start_idx = self.index
            self.index = (self.index + 1) % n

            ordered = [self.keys[(start_idx + i) % n] for i in range(n)]
            active = [k for k in ordered if self.key_stats.get(k, {}).get("cooldown_until", 0) <= now]
            in_cooldown = [k for k in ordered if self.key_stats.get(k, {}).get("cooldown_until", 0) > now]
            in_cooldown.sort(key=lambda k: self.key_stats.get(k, {}).get("cooldown_until", 0))

            return active + in_cooldown

    def mark_rate_limited(self, key: str, cooldown_seconds: float = 60.0):
        with self.lock:
            if key in self.key_stats:
                self.key_stats[key]["cooldown_until"] = time.time() + cooldown_seconds
                self.key_stats[key]["errors"] += 1
                self.key_stats[key]["status"] = "cooldown"
                print(f"🔄 [Key Pool] Key {key[:12]}... hit limit. Shifted to cooldown ({cooldown_seconds}s). Next key will take over.")

    def record_success(self, key: str, approx_tokens: int = 500):
        with self.lock:
            if key in self.key_stats:
                st = self.key_stats[key]
                st["requests"] += 1
                st["tokens_estimated"] += approx_tokens
                if st["tokens_estimated"] >= 35000:
                    st["cooldown_until"] = time.time() + 25
                    st["tokens_estimated"] = 0
                    print(f"🔄 [Key Pool] Key {key[:12]}... high token volume. Shifting to other pool keys for 25s.")

    def get_pool_status(self) -> dict:
        with self.lock:
            now = time.time()
            return {
                "total_keys": len(self.keys),
                "keys": [
                    {
                        "index": idx + 1,
                        "key_mask": f"{k[:10]}...{k[-5:]}",
                        "requests": self.key_stats.get(k, {}).get("requests", 0),
                        "errors": self.key_stats.get(k, {}).get("errors", 0),
                        "status": "cooling_down" if self.key_stats.get(k, {}).get("cooldown_until", 0) > now else "active",
                        "cooldown_remaining_seconds": max(0, int(self.key_stats.get(k, {}).get("cooldown_until", 0) - now))
                    }
                    for idx, k in enumerate(self.keys)
                ]
            }

gemini_key_pool = GeminiKeyPool()

def get_default_api_key() -> str:
    candidates = gemini_key_pool.get_candidate_keys()
    return candidates[0] if candidates else ""

# Initialize FastAPI App
app = FastAPI(
    title="XortLogix High Level Assistant",
    description="ChatGPT-Style interface powered by ChromaDB Vector Store, Gemini API & Production Auth",
    version="3.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Vercel Path Restoration Middleware
@app.middleware("http")
async def vercel_path_rewrite_middleware(request: Request, call_next):
    try:
        orig_path = (
            request.headers.get("x-invoke-path")
            or request.headers.get("x-forwarded-uri")
            or request.headers.get("x-original-uri")
            or request.headers.get("x-real-origin-path")
        )
        if not orig_path:
            matched = request.headers.get("x-matched-path")
            if matched and ":" not in matched and "(" not in matched and "*" not in matched:
                orig_path = matched

        if orig_path:
            clean_path = orig_path.split("?")[0]
            # Only rewrite if current path is generic entrypoint or missing route
            if request.scope.get("path") in ["/api/index.py", "/api/index", "/api", "/api/", "/index.py", "/"]:
                request.scope["path"] = clean_path
    except Exception as e:
        print(f"Path rewrite note: {e}")
    return await call_next(request)

# Mount Static Assets Directory (Only in non-Vercel local environments; Vercel serves static files via Edge CDN)
STATIC_DIR = os.path.join(BASE_DIR, "static")
if not IS_VERCEL and os.path.exists(STATIC_DIR):
    try:
        app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    except Exception as e:
        print(f"StaticFiles mount note: {e}")

# Global Variables for Lazy Connections with Thread-Safety
import threading
_chroma_lock = threading.Lock()
_embed_lock = threading.Lock()
client_chroma = None
collection = None
embed_model = None

def get_chroma_collection():
    global client_chroma, collection
    if collection is not None and collection is not False:
        return collection
    with _chroma_lock:
        if collection is None or collection is False:
            try:
                ensure_chroma_db_on_vercel()
                import chromadb
                print("📦 Connecting to Local ChromaDB...")
                client_chroma = chromadb.PersistentClient(path=LOCAL_DB_PATH)
                collection = client_chroma.get_collection(name="ghl_knowledge_base")
                print(f"✅ ChromaDB collection loaded. Chunks: {collection.count()}")
            except Exception as e:
                print(f"ℹ️ ChromaDB initialization note: {e}")
                return None
    return collection

def get_embedding_model():
    global embed_model
    if embed_model is not None and embed_model is not False:
        return embed_model
    with _embed_lock:
        if embed_model is None or embed_model is False:
            # 1. Try FastEmbed (Ultra-fast C++ ONNX Runtime, ~50MB RAM)
            try:
                from fastembed import TextEmbedding
                print("🚀 Loading FastEmbed (nomic-ai/nomic-embed-text-v1.5) ONNX (threads=1)...")
                embed_model = TextEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5", threads=1)
                print("✅ FastEmbed ONNX model ready!")
                return embed_model
            except Exception as e_fe:
                print(f"ℹ️ FastEmbed fallback note: {e_fe}")

            # 2. Try SentenceTransformer (PyTorch)
            try:
                try:
                    import torch
                    torch.set_num_threads(2)
                    if hasattr(torch, "set_num_interop_threads"):
                        torch.set_num_interop_threads(1)
                except Exception:
                    pass
                from sentence_transformers import SentenceTransformer
                print("🔄 Loading SentenceTransformer Embedding Model (nomic-ai/nomic-embed-text-v1.5)...")
                embed_model = SentenceTransformer('nomic-ai/nomic-embed-text-v1.5', trust_remote_code=True)
                print("✅ SentenceTransformer model ready!")
                return embed_model
            except Exception as e:
                print(f"ℹ️ SentenceTransformer fallback note: {e}")
                return None
    return embed_model

def _warmup_background():
    import gc
    try:
        db.init_db()
        print("✅ Database tables initialized.")
    except Exception as e:
        print(f"ℹ️ Database init note: {e}")
        
    try:
        col = get_chroma_collection()
        if col:
            print(f"✅ ChromaDB ready with {col.count()} chunks.")
    except Exception as e:
        print(f"ℹ️ ChromaDB startup note: {e}")

    try:
        model = get_embedding_model()
        if model:
            print("⚡ Pre-warming embedding model for instant queries...")
            if hasattr(model, 'embed'):
                _ = list(model.embed(["search_query: GoHighLevel warmup query"]))
            else:
                try:
                    import torch
                    with torch.inference_mode():
                        _ = model.encode("search_query: GoHighLevel warmup query")
                except Exception:
                    _ = model.encode("search_query: GoHighLevel warmup query")
            print("🚀 Embedding model warmed up and ready for instant requests!")
    except Exception as e:
        print(f"ℹ️ Embedding startup warmup note: {e}")
    gc.collect()

@app.on_event("startup")
async def startup_event():
    if not IS_VERCEL:
        print("🚀 FastAPI server started. Initializing background warmup...")
        threading.Thread(target=_warmup_background, daemon=True).start()

# Auth Dependency
def get_current_user(ghl_session: Optional[str] = Cookie(None), authorization: Optional[str] = Header(None)):
    token = ghl_session
    if not token and authorization:
        if authorization.startswith("Bearer "):
            token = authorization.split(" ", 1)[1].strip()
        else:
            token = authorization.strip()
    
    user = db.get_user_from_session(token) if token else None
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required. Please log in.")
    return user

def get_optional_user(ghl_session: Optional[str] = Cookie(None), authorization: Optional[str] = Header(None)):
    token = ghl_session
    if not token and authorization:
        if authorization.startswith("Bearer "):
            token = authorization.split(" ", 1)[1].strip()
        else:
            token = authorization.strip()
    return db.get_user_from_session(token) if token else None

# Pydantic Schemas

class LoginRequest(BaseModel):
    email: str
    password: str

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str

class RenameConvRequest(BaseModel):
    title: str

class AttachmentItem(BaseModel):
    name: str
    type: str = "other"  # 'image', 'audio', 'document', 'text'
    mime_type: str = "application/octet-stream"
    data: str  # base64 string or data: URL
    size: Optional[int] = 0

class ChatRequest(BaseModel):
    query: Optional[str] = ""
    conversation_id: Optional[str] = None
    top_k: Optional[int] = 1
    api_key: Optional[str] = None
    attachments: Optional[List[AttachmentItem]] = []
    selected_model: Optional[str] = "gemini-3.6-flash"

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
    query_time_ms: float
    top_k: int
    conversation_id: str
    conversation_title: str
    model: str = "gemini-3.6-flash"

class KeyValidateRequest(BaseModel):
    api_key: str

# Web App Route & Health Check
@app.get("/")
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return JSONResponse(content={"status": "online", "service": "XortLogix High Level Assistant"})

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)

@app.get("/health")
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "XortLogix High Level Assistant"}

api_router = APIRouter()

@api_router.get("/status")
async def get_system_status():
    try:
        col = get_chroma_collection()
        count = col.count() if col else 5379
    except Exception:
        count = 5379
        
    return {
        "status": "online",
        "total_chunks": count,
        "collection": "ghl_knowledge_base",
        "embedding_model": "nomic-embed-text-v1.5",
        "gemini_model": "gemini-3.6-flash",
        "has_default_key": bool(get_default_api_key() and get_default_api_key() != "YOUR_GEMINI_API_KEY_HERE")
    }

# Authentication Endpoints

@api_router.post("/auth/login")
async def login(req: LoginRequest, response: Response):
    if not req.email.strip() or not req.password:
        raise HTTPException(status_code=400, detail="Email and password are required.")

    user = db.authenticate_user(req.email, req.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    session_token = db.create_session(user['id'])
    response.set_cookie(
        key="ghl_session",
        value=session_token,
        httponly=True,
        samesite="lax",
        path="/",
        max_age=30 * 24 * 3600
    )
    return {"user": user, "token": session_token, "is_admin": user["email"] == ADMIN_EMAIL}

@api_router.get("/auth/me")
async def get_me(user: dict = Depends(get_current_user)):
    return {"user": user, "is_admin": user["email"] == ADMIN_EMAIL}

@api_router.post("/auth/logout")
async def logout(response: Response, ghl_session: Optional[str] = Cookie(None)):
    if ghl_session:
        db.delete_session(ghl_session)
    response.delete_cookie("ghl_session", path="/")
    return {"message": "Logged out successfully"}

class UpdateProfileRequest(BaseModel):
    name: str

@api_router.post("/auth/update-profile")
async def update_user_profile(req: UpdateProfileRequest, user: dict = Depends(get_current_user)):
    if not req.name or not req.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    try:
        updated_user = db.update_user_name(user['id'], req.name.strip())
        return {"user": updated_user, "message": "Profile updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/auth/change-password")
async def change_user_password(req: ChangePasswordRequest, user: dict = Depends(get_current_user)):
    if len(req.new_password) < 6:
        raise HTTPException(status_code=400, detail="New password must be at least 6 characters long.")
    try:
        db.update_password(user['id'], req.old_password, req.new_password)
        return {"message": "Password updated successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


ADMIN_EMAIL = "muhammad.okasha2146@gmail.com"

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@api_router.get("/admin/users")
async def admin_get_users(user: dict = Depends(get_current_user)):
    if user['email'] != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"users": db.get_all_users()}

@api_router.post("/admin/users")
async def admin_create_user(req: CreateUserRequest, user: dict = Depends(get_current_user)):
    if user['email'] != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        new_user = db.create_user(req.name, req.email, req.password)
        return {"user": new_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.delete("/admin/users/{target_id}")
async def admin_delete_user(target_id: str, user: dict = Depends(get_current_user)):
    if user['email'] != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Forbidden")
    if target_id == user['id']:
        raise HTTPException(status_code=400, detail="Cannot delete yourself")
    success = db.delete_user(target_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# Conversation History Endpoints
@api_router.get("/conversations")
async def list_conversations(user: dict = Depends(get_current_user)):
    conversations = db.get_user_conversations(user['id'])
    return {"conversations": conversations}

@api_router.post("/conversations")
async def create_new_conversation(user: dict = Depends(get_current_user)):
    conv = db.create_conversation(user['id'], title="New Chat")
    return {"conversation": conv}

@api_router.get("/conversations/{conv_id}")
async def get_conversation(conv_id: str, user: dict = Depends(get_current_user)):
    details = db.get_conversation_details(conv_id, user['id'])
    if not details:
        raise HTTPException(status_code=404, detail="Conversation not found or access denied.")
    return {"conversation": details}

@api_router.put("/conversations/{conv_id}")
async def rename_conv(conv_id: str, req: RenameConvRequest, user: dict = Depends(get_current_user)):
    if not req.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty.")
    success = db.rename_conversation(conv_id, user['id'], req.title)
    if not success:
        raise HTTPException(status_code=404, detail="Conversation not found or access denied.")
    return {"message": "Conversation renamed successfully", "title": req.title.strip()}

@api_router.post("/conversations/{conv_id}/pin")
async def toggle_pin(conv_id: str, user: dict = Depends(get_current_user)):
    is_pinned = db.toggle_pin_conversation(conv_id, user['id'])
    return {"is_pinned": is_pinned}

@api_router.delete("/conversations/{conv_id}")
async def delete_conv(conv_id: str, user: dict = Depends(get_current_user)):
    success = db.delete_conversation(conv_id, user['id'])
    if not success:
        raise HTTPException(status_code=404, detail="Conversation not found or access denied.")
    return {"message": "Conversation deleted successfully"}

# RAG Chat Endpoint (Live Real-Time Streaming & Multimodal Support)
@api_router.post("/chat")
async def chat_rag_endpoint(request: ChatRequest, user: dict = Depends(get_current_user)):
    user_query = (request.query or "").strip()
    attachments = request.attachments or []

    if not user_query and not attachments:
        raise HTTPException(status_code=400, detail="Query string or attached file/voice input is required.")
    
    # 1. Resolve or Create Conversation
    conv_id = request.conversation_id
    if conv_id:
        conv_details = db.get_conversation_details(conv_id, user['id'])
        if not conv_details:
            conv = db.create_conversation(user['id'], title="New Chat")
            conv_id = conv['id']
    else:
        conv = db.create_conversation(user['id'], title="New Chat")
        conv_id = conv['id']

    # Auto-synthesize query if text is empty but attachments are present
    if not user_query and attachments:
        has_audio = any(a.type == 'audio' or (a.mime_type and a.mime_type.startswith('audio/')) for a in attachments)
        has_image = any(a.type == 'image' or (a.mime_type and a.mime_type.startswith('image/')) for a in attachments)
        if has_audio:
            user_query = "Please listen to the attached voice message / audio note carefully, transcribe what is said, and provide a clear, comprehensive answer and GoHighLevel technical guidance."
        elif has_image:
            user_query = "Please analyze the attached image(s) / screenshot(s) in detail. Explain what is shown, identify any relevant GoHighLevel workflows, settings, or errors, and provide step-by-step guidance."
        else:
            user_query = "Please analyze the attached file(s) / document(s) and provide a detailed explanation and answers based on GoHighLevel technical capabilities."

    # 2. Save User Message with Attachments
    att_save_data = []
    for a in attachments:
        att_save_data.append({
            "name": a.name,
            "type": a.type,
            "mime_type": a.mime_type,
            "size": a.size,
            "data": a.data
        })
    user_msg_record = db.add_message(conv_id, user['id'], 'user', user_query, attachments=att_save_data)
    current_conv_title = user_msg_record['conversation_title']

    # 3. Resolve API Keys from Polling Pool (Prioritize request key from user settings if provided)
    req_key = (request.api_key or "").strip()
    candidate_keys = gemini_key_pool.get_candidate_keys(override_key=req_key)
    
    if not candidate_keys:
        raise HTTPException(
            status_code=401, 
            detail="Gemini API Key is not configured on server. Please set GEMINI_API_KEYS in the server .env file."
        )
    
    start_time = time.time()

    # Extract user's first name for personalization
    user_name = user.get('name') or (user.get('email', '').split('@')[0] if user.get('email') else 'there')
    first_name = user_name.split()[0].capitalize() if user_name else 'there'
    
    # Check if conversation already has prior messages (don't repeat greeting name in every reply)
    prior_messages = db.get_conversation_messages(conv_id, user['id']) if conv_id else []
    is_first_message = len(prior_messages) <= 1

    top_k = 1

    def get_conversational_reply(query_lower: str, name: str, is_first: bool) -> str:
        if any(k in query_lower for k in ["salam", "aoa", "assalam"]):
            if is_first:
                return f"Walaikum Assalam {name}! 🤝 I'm your XortLogix High Level AI Technical Assistant. How can I help you today with your GoHighLevel workflows, funnels, APIs, or CRM automations?"
            else:
                return "Walaikum Assalam! 🤝 How can I assist you with your GoHighLevel setup or workflow?"
        
        elif "good morning" in query_lower:
            return f"Good morning{f', {name}' if is_first else ''}! ☀️ How can I assist you with your GoHighLevel setups or workflows today?"
        
        elif "good afternoon" in query_lower:
            return f"Good afternoon{f', {name}' if is_first else ''}! 🌤️ How can I assist you with your GoHighLevel automations today?"
        
        elif "good evening" in query_lower:
            return f"Good evening{f', {name}' if is_first else ''}! 🌙 How can I assist you with GoHighLevel features or CRM settings today?"
        
        elif "how are you" in query_lower or "how r u" in query_lower:
            return f"I'm doing great{f', {name}' if is_first else ''}, thank you for asking! 😊 What can I help you with regarding GoHighLevel today?"
        
        elif any(k in query_lower for k in ["learn", "teach"]):
            if is_first:
                return f"Hello {name}! 👋 Certainly, I'd be glad to help you learn. Please let me know what specific GoHighLevel topic you'd like to explore (e.g. Workflows, Triggers, Custom Values, Funnels, APIs, or Sub-accounts)!"
            else:
                return "Certainly! Please go ahead and share what specific GoHighLevel topic or workflow you'd like to learn, and I'll explain it step by step."
        
        elif any(k in query_lower for k in ["question", "ask"]):
            if is_first:
                return f"Hello {name}! 👋 Of course! Please feel free to ask your question regarding GoHighLevel features, workflows, or technical configurations."
            else:
                return "Of course! Please go ahead and ask your question, and I'll be glad to assist you."
        
        elif any(k in query_lower for k in ["who are you", "what can you do", "about yourself"]):
            prefix = f"Hello {name}! 👋 " if is_first else ""
            return f"{prefix}I am your dedicated **XortLogix High Level Technical Assistant**.\n\nI can help you with:\n- ⚡ **Workflow Automations & Custom Triggers**\n- 🔄 **REST APIs, Webhooks & Custom Values**\n- 🏗️ **Funnels, Websites & Form Builders**\n- 👥 **Contacts, Pipelines, Sub-accounts & CRM Settings**\n\nFeel free to ask any question regarding GoHighLevel!"
        
        else:
            if is_first:
                return f"Hello {name}! 👋 I'm your XortLogix High Level AI Technical Assistant. How can I help you today with GoHighLevel workflows, funnels, APIs, or CRM settings?"
            else:
                return "How can I assist you further with your GoHighLevel setup or technical questions?"

    async def stream_generator():
        from google import genai
        from google.genai import types
        # Send initial metadata immediately to establish active HTTP connection with Railway proxy
        yield f"data: {json.dumps({'type': 'meta', 'conversation_id': conv_id, 'conversation_title': current_conv_title})}\n\n"

        try:
            # 1. Parse and extract text / multimodal parts from ANY file type
            gemini_parts = []
            extracted_doc_text = ""

            for att in attachments:
                try:
                    raw_b64 = att.data
                    if ";base64," in raw_b64:
                        raw_b64 = raw_b64.split(";base64,")[1]
                    raw_bytes = base64.b64decode(raw_b64)

                    # Universal extraction for ANY file type: PDF, Word, Excel, PPTX, Code, Text, ZIP, Audio, Video, Image, etc.
                    file_info = extract_file_content(att.name, raw_bytes, att.mime_type)
                    m_type = file_info["mime_type"]

                    # Append extracted textual/tabular/structural content to prompt
                    if file_info["text"]:
                        extracted_doc_text += f"\n\n--- [Attached Document: {att.name} ({file_info['file_type'].upper()})] ---\n{file_info['text'][:30000]}\n--- [End of {att.name}] ---\n"

                    # If multimodal (image, audio, video, pdf), pass raw bytes to Gemini API Part
                    if file_info["is_multimodal"] or m_type.startswith(("image/", "audio/", "video/", "application/pdf")):
                        try:
                            part = types.Part.from_bytes(data=raw_bytes, mime_type=m_type)
                            gemini_parts.append(part)
                        except Exception as e_part:
                            print(f"ℹ️ Gemini multimodal part note ({att.name}): {e_part}")
                except Exception as e_att:
                    print(f"⚠️ Error preparing attachment {att.name}: {e_att}")

            # 2. Intelligent RAG Pipeline Execution
            col = get_chroma_collection()
            model = get_embedding_model()
            analysis, prompt, source_labels = RAGEngine.process_query(
                user_query=user_query,
                chroma_col=col,
                embed_model=model,
                user_name=first_name,
                is_first_message=is_first_message,
                top_k=top_k,
                history=prior_messages
            )

            # Instant zero-latency streaming for pure conversational openers (when no files attached)
            if analysis.is_conversational and not attachments:
                reply_text = get_conversational_reply(analysis.cleaned_query, first_name, is_first_message)
                words = reply_text.split(" ")
                for i, w in enumerate(words):
                    chunk = w if i == len(words) - 1 else w + " "
                    yield f"data: {json.dumps({'type': 'chunk', 'text': chunk})}\n\n"
                    await asyncio.sleep(0.012)

                db.add_message(conv_id, user['id'], 'assistant', reply_text, sources=[])
                elapsed_ms = round((time.time() - start_time) * 1000, 2)
                yield f"data: {json.dumps({'type': 'done', 'model': 'instant-conversational', 'elapsed_ms': elapsed_ms, 'conversation_id': conv_id, 'conversation_title': current_conv_title})}\n\n"
                return

            # Append document extracted context to prompt if available
            final_prompt_text = prompt
            if extracted_doc_text:
                final_prompt_text += f"\n\n### User Provided Attachments / Context Documents:\n{extracted_doc_text}"

            # Assemble contents for Gemini (Prompt Text + Multimodal Parts)
            contents_payload = [types.Part.from_text(text=final_prompt_text)] + gemini_parts

            # Multi-Key Polling & Automatic Failover Engine
            full_text = ""
            used_model = "gemini-3.6-flash"
            stream_success = False
            last_error = ""

            gen_config = types.GenerateContentConfig(
                temperature=0.2,
                top_p=0.95
            )

            pref_model = (getattr(request, 'selected_model', 'gemini-3.6-flash') or 'gemini-3.6-flash').strip()

            # Iterate through candidate keys in polling order
            for key_idx, current_key in enumerate(candidate_keys):
                try:
                    client_gemini = genai.Client(api_key=current_key)
                    
                    # Discover models or use modern flash tier (ordered by stability and current availability)
                    fallback_models = [
                        "gemini-3.6-flash",
                        "gemini-3.7-flash",
                        "gemini-3.5-flash-lite",
                        "gemini-flash-latest",
                        "gemini-3.5-flash",
                        "gemini-flash-lite-latest",
                        "gemini-pro-latest"
                    ]
                    if pref_model and pref_model != "auto":
                        if pref_model in fallback_models:
                            fallback_models.remove(pref_model)
                        fallback_models.insert(0, pref_model)

                    fallback_models = list(dict.fromkeys(fallback_models))
                    key_exhausted = False

                    for mod_name in fallback_models:
                        try:
                            response_stream = client_gemini.models.generate_content_stream(
                                model=mod_name,
                                contents=contents_payload,
                                config=gen_config
                            )
                            used_model = mod_name
                            chunk_received = False
                            for chunk in response_stream:
                                if chunk and chunk.text:
                                    chunk_received = True
                                    full_text += chunk.text
                                    yield f"data: {json.dumps({'type': 'chunk', 'text': chunk.text})}\n\n"
                            
                            if full_text:
                                stream_success = True
                                gemini_key_pool.record_success(current_key, approx_tokens=len(full_text) // 3)
                                break
                        except Exception as e_stream:
                            last_error = str(e_stream)
                            err_low = last_error.lower()

                            # 1. Temporary model capacity overload (503 / spikes in demand / high demand)
                            # CRITICAL: This is a MODEL issue, NOT a key issue! DO NOT break key, try next model!
                            if any(term in err_low for term in ["503", "spikes in demand", "high demand", "unavailable"]):
                                print(f"⚠️ [Model Spike] Model {mod_name} returned 503 high demand. Auto-falling back to next model on same key...")
                                full_text = ""
                                continue

                            # 2. Genuine Key Quota Exhaustion (429 / resource_exhausted / quota)
                            elif any(term in err_low for term in ["429", "resource_exhausted", "quota", "rate_limit"]):
                                gemini_key_pool.mark_rate_limited(current_key, cooldown_seconds=60)
                                key_exhausted = True
                                print(f"⚠️ [Key Pool] Key {current_key[:12]}... quota-limited on {mod_name}. Shifting immediately to next pool key...")
                                break

                            # 3. Model not found or deprecated (404)
                            elif any(term in err_low for term in ["404", "not_found"]):
                                print(f"ℹ️ Model {mod_name} not available (404), trying next model in tier...")
                                full_text = ""
                                continue

                            else:
                                print(f"ℹ️ Model {mod_name} error: {e_stream}, trying next model in tier...")
                                full_text = ""
                                continue

                    if stream_success:
                        break

                    # Fallback non-streaming attempt on current key if not quota-limited
                    if not key_exhausted and not stream_success:
                        for mod_name in fallback_models:
                            try:
                                resp = client_gemini.models.generate_content(
                                    model=mod_name,
                                    contents=contents_payload,
                                    config=gen_config
                                )
                                if resp and resp.text:
                                    full_text = resp.text
                                    used_model = mod_name
                                    yield f"data: {json.dumps({'type': 'chunk', 'text': full_text})}\n\n"
                                    stream_success = True
                                    gemini_key_pool.record_success(current_key, approx_tokens=len(full_text) // 3)
                                    break
                            except Exception as e_gen:
                                last_error = str(e_gen)
                                err_low = last_error.lower()
                                if any(term in err_low for term in ["503", "spikes in demand", "high demand", "unavailable", "404", "not_found"]):
                                    continue
                                elif any(term in err_low for term in ["429", "resource_exhausted", "quota", "rate_limit"]):
                                    gemini_key_pool.mark_rate_limited(current_key, cooldown_seconds=60)
                                    break
                                else:
                                    continue

                    if stream_success:
                        break

                except Exception as e_client:
                    last_error = str(e_client)
                    if any(term in last_error.lower() for term in ["429", "quota", "resource_exhausted"]):
                        gemini_key_pool.mark_rate_limited(current_key, cooldown_seconds=60)

            if not stream_success or not full_text:
                err_detail = f" Details: `{last_error}`" if last_error else ""
                
                if "503" in last_error or "high demand" in last_error.lower() or "spikes in demand" in last_error.lower():
                    help_text = "\n\n💡 Google Gemini is currently experiencing temporary high server traffic. Automatic failover has been enabled. Please submit your prompt again."
                elif "404" in last_error or "NOT_FOUND" in last_error:
                    help_text = "\n\n💡 **Diagnosis**: Model access unavailable. Falling back to active key pool."
                else:
                    help_text = "\n\nPlease verify that your Gemini API keys in .env are active."

                error_msg = f"⚠️ I was unable to complete the request with the available API keys.{err_detail}{help_text}"
                yield f"data: {json.dumps({'type': 'chunk', 'text': error_msg})}\n\n"
                db.add_message(conv_id, user['id'], 'assistant', error_msg, sources=[])
                yield f"data: {json.dumps({'type': 'done', 'model': 'error-fallback', 'elapsed_ms': 0, 'conversation_id': conv_id, 'conversation_title': current_conv_title})}\n\n"
                return

            # Save sanitized assistant message to DB
            sanitized_text = clean_latex_artifacts(full_text)
            db.add_message(conv_id, user['id'], 'assistant', sanitized_text, sources=source_labels)
            elapsed_ms = round((time.time() - start_time) * 1000, 2)

            yield f"data: {json.dumps({'type': 'done', 'model': used_model, 'elapsed_ms': elapsed_ms, 'conversation_id': conv_id, 'conversation_title': current_conv_title})}\n\n"

        except Exception as e_global:
            print(f"❌ Error in chat stream: {e_global}")
            yield f"data: {json.dumps({'type': 'chunk', 'text': f'⚠️ **Error:** {str(e_global)}'})}\n\n"
            yield f"data: {json.dumps({'type': 'done', 'model': 'error', 'elapsed_ms': 0, 'conversation_id': conv_id, 'conversation_title': current_conv_title})}\n\n"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")

@api_router.post("/validate-key")
async def validate_api_key(req: KeyValidateRequest):
    key = req.api_key.strip()
    if not key:
        return {"valid": False, "message": "Key is empty"}
    try:
        from google import genai
        client = genai.Client(api_key=key)
        client.models.generate_content(
            model='gemini-3.6-flash',
            contents='Ping'
        )
        return {"valid": True, "message": "API key validated successfully."}
    except Exception as e:
        return {"valid": False, "message": str(e)}

@api_router.get("/key-pool/status")
async def get_key_pool_status():
    """
    Returns current health, request distribution, and cooldown status across all keys in the pool.
    """
    return gemini_key_pool.get_pool_status()

@api_router.post("/knowledge/upload")
async def upload_knowledge_file(
    file: UploadFile = File(...),
    current_user: Optional[dict] = Depends(get_optional_user)
):
    """
    Universal Knowledge Base File Ingestion:
    Uploads ANY document type (PDF, Word DOCX, Excel XLSX/CSV, PowerPoint PPTX, Text, Code, etc.)
    extracts all content, chunks semantically, and upserts embeddings into ChromaDB.
    """
    try:
        content = await file.read()
        extracted = extract_file_content(file.filename, content, file.content_type)
        extracted_text = extracted.get("text", "")

        if not extracted_text or len(extracted_text.strip()) < 30:
            return JSONResponse(status_code=400, content={
                "status": "error",
                "message": f"Could not extract sufficient text from '{file.filename}'. Please ensure the file contains readable text or tabular data."
            })

        # Split into semantic word-bounded chunks
        paragraphs = [p.strip() for p in extracted_text.split("\n\n") if p.strip()]
        chunks = []
        curr = []
        curr_len = 0
        for p in paragraphs:
            w_count = len(p.split())
            if curr_len + w_count <= 250:
                curr.append(p)
                curr_len += w_count
            else:
                if curr:
                    chunks.append("\n\n".join(curr))
                curr = [p]
                curr_len = w_count
        if curr:
            chunks.append("\n\n".join(curr))

        # Save copy into knowledge_uploads directory
        uploads_dir = "/tmp/knowledge_uploads" if IS_VERCEL else os.path.join(BASE_DIR, "knowledge_uploads")
        os.makedirs(uploads_dir, exist_ok=True)
        save_path = os.path.join(uploads_dir, file.filename)
        with open(save_path, "wb") as f:
            f.write(content)

        # Upsert into ChromaDB
        col = get_chroma_collection()
        embed_model = get_embedding_model()

        chunk_ids = []
        chunk_docs = []
        chunk_metas = []

        for idx, chunk in enumerate(chunks):
            c_id = hashlib.md5(f"{file.filename}_{idx}_{chunk[:40]}".encode('utf-8')).hexdigest()
            chunk_ids.append(c_id)
            chunk_docs.append(chunk)
            chunk_metas.append({
                "source": file.filename,
                "title": f"{file.filename} (Part {idx+1})",
                "file_type": extracted["file_type"],
                "uploaded_by": current_user.get("email", "admin") if current_user else "admin",
                "uploaded_at": str(time.time())
            })

        # Compute embeddings with nomic search_document prefix
        if hasattr(embed_model, 'embed'):
            embs = [e.tolist() if hasattr(e, 'tolist') else list(e) for e in embed_model.embed([f"search_document: {c}" for c in chunk_docs])]
        elif hasattr(embed_model, 'encode'):
            embs = embed_model.encode([f"search_document: {c}" for c in chunk_docs]).tolist()
        else:
            embs = None

        if embs:
            col.upsert(ids=chunk_ids, documents=chunk_docs, embeddings=embs, metadatas=chunk_metas)
        else:
            col.upsert(ids=chunk_ids, documents=chunk_docs, metadatas=chunk_metas)

        total_chunks = col.count() if hasattr(col, 'count') else len(chunk_ids)

        return {
            "status": "success",
            "message": f"Successfully indexed '{file.filename}' into the ChromaDB Knowledge Base!",
            "filename": file.filename,
            "file_type": extracted["file_type"],
            "chunks_indexed": len(chunk_ids),
            "total_db_chunks": total_chunks
        }
    except Exception as e:
        print(f"❌ Knowledge upload error: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

# Mount APIRouter with and without /api prefix
app.include_router(api_router, prefix="/api")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    print("🚀 Launching GoHighLevel RAG ChatGPT Application on http://127.0.0.1:7860 ...")
    uvicorn.run(app, host="127.0.0.1", port=7860)
