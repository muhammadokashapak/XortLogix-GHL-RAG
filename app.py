import os
import sys

# Vercel pysqlite3 override for ChromaDB SQLite compatibility
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

import asyncio
import json
import time
import base64
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request, Response, Depends, Cookie, Header, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, EmailStr
SentenceTransformer = None
from dotenv import load_dotenv

import db
from rag_engine import RAGEngine, QueryUnderstandingEngine, clean_latex_artifacts

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
if IS_VERCEL:
    LOCAL_DB_PATH = "/tmp/ghl_chroma_db"
    src_db = os.path.join(BASE_DIR, "ghl_chroma_db")
    if not os.path.exists(LOCAL_DB_PATH) and os.path.exists(src_db):
        import shutil
        try:
            shutil.copytree(src_db, LOCAL_DB_PATH)
        except Exception as e:
            print(f"Copying ChromaDB to /tmp failed: {e}")
else:
    LOCAL_DB_PATH = os.path.join(BASE_DIR, "ghl_chroma_db")

DEFAULT_GEMINI_KEY = os.getenv("GEMINI_API_KEY", "").strip()

def get_default_api_key() -> str:
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key or key == "YOUR_GEMINI_API_KEY_HERE":
        if os.path.exists(ENV_PATH):
            try:
                with open(ENV_PATH, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GEMINI_API_KEY="):
                            k = line.split("=", 1)[1].strip()
                            if k:
                                return k
            except Exception:
                pass
        return DEFAULT_GEMINI_KEY
    return key

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
    # In Vercel serverless, retrieve the actual requested path from forwarding headers
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
    return await call_next(request)

# Mount Static Assets Directory
STATIC_DIR = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

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

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
    query_time_ms: float
    top_k: int
    conversation_id: str
    conversation_title: str
    model: str = "gemini-2.5-flash"

class KeyValidateRequest(BaseModel):
    api_key: str

# Web App Route & Health Check
@app.get("/")
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="static/index.html not found.")
    return FileResponse(index_path)

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

    # 3. Resolve API Key (Always prioritize server .env key)
    default_key = get_default_api_key()
    req_key = (request.api_key or "").strip()
    api_key = default_key if default_key else req_key

    if not api_key or api_key == "YOUR_GEMINI_API_KEY_HERE":
        raise HTTPException(
            status_code=401, 
            detail="Gemini API Key is missing. Please configure your API key in Settings or set GEMINI_API_KEY in environment."
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
            # 1. Parse and prepare Multimodal Gemini Parts
            gemini_parts = []
            extracted_doc_text = ""

            for att in attachments:
                try:
                    raw_b64 = att.data
                    if ";base64," in raw_b64:
                        raw_b64 = raw_b64.split(";base64,")[1]
                    raw_bytes = base64.b64decode(raw_b64)
                    m_type = att.mime_type.lower() if att.mime_type else "application/octet-stream"

                    # Normalize common audio/video types
                    if m_type == "audio/x-m4a" or att.name.endswith(".m4a"):
                        m_type = "audio/mp4"
                    elif m_type == "audio/mp3":
                        m_type = "audio/mpeg"

                    # Extract plain text from text documents for RAG context
                    if m_type.startswith("text/") or att.name.endswith(('.txt', '.csv', '.json', '.md', '.log', '.xml', '.html', '.js', '.py')):
                        try:
                            decoded_txt = raw_bytes.decode('utf-8', errors='replace')
                            extracted_doc_text += f"\n\n--- [Attached File Content: {att.name}] ---\n{decoded_txt[:15000]}\n--- [End of {att.name}] ---\n"
                        except Exception:
                            pass

                    # Extract text from PDF files using pypdf
                    if m_type == "application/pdf" or att.name.endswith(".pdf"):
                        m_type = "application/pdf"
                        try:
                            import pypdf
                            import io
                            pdf_reader = pypdf.PdfReader(io.BytesIO(raw_bytes))
                            pdf_text = ""
                            for page in pdf_reader.pages:
                                page_txt = page.extract_text()
                                if page_txt:
                                    pdf_text += page_txt + "\n"
                            if pdf_text:
                                extracted_doc_text += f"\n\n--- [Extracted PDF Document Content: {att.name}] ---\n{pdf_text[:20000]}\n--- [End of {att.name}] ---\n"
                        except Exception as e_pdf:
                            print(f"ℹ️ PDF text extraction fallback note: {e_pdf}")

                    part = types.Part.from_bytes(data=raw_bytes, mime_type=m_type)
                    gemini_parts.append(part)
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

            client_gemini = genai.Client(api_key=api_key)
            fallback_models = [
                "gemini-3.6-flash",
                "gemini-flash-latest",
                "gemini-flash-lite-latest",
                "gemini-3.5-flash"
            ]

            full_text = ""
            used_model = "gemini-3.6-flash"
            stream_success = False

            gen_config = types.GenerateContentConfig(
                temperature=0.2,
                top_p=0.95
            )

            for mod_name in fallback_models:
                try:
                    response_stream = client_gemini.models.generate_content_stream(
                        model=mod_name,
                        contents=contents_payload,
                        config=gen_config
                    )
                    used_model = mod_name
                    for chunk in response_stream:
                        if chunk and chunk.text:
                            full_text += chunk.text
                            yield f"data: {json.dumps({'type': 'chunk', 'text': chunk.text})}\n\n"
                    
                    if full_text:
                        stream_success = True
                        break
                except Exception as e_stream:
                    print(f"ℹ️ Stream model {mod_name} error: {e_stream}, trying next fallback...")
                    full_text = ""

            # Fallback to non-streaming if stream didn't yield text
            if not stream_success:
                for mod_name in fallback_models:
                    try:
                        resp = client_gemini.models.generate_content(
                            model=mod_name,
                            contents=contents_payload,
                        )
                        if resp and resp.text:
                            full_text = resp.text
                            used_model = mod_name
                            yield f"data: {json.dumps({'type': 'chunk', 'text': full_text})}\n\n"
                            stream_success = True
                            break
                    except Exception as e_gen:
                        print(f"ℹ️ Generate content error on {mod_name}: {e_gen}")

            if not stream_success or not full_text:
                error_msg = "⚠️ I was unable to reach the AI model service. Please check your Gemini API key in Settings or try again in a few moments."
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

# Mount APIRouter with and without /api prefix
app.include_router(api_router, prefix="/api")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    print("🚀 Launching GoHighLevel RAG ChatGPT Application on http://127.0.0.1:7860 ...")
    uvicorn.run(app, host="127.0.0.1", port=7860)
