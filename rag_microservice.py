import os
import sys
import time
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb
from google import genai
from dotenv import load_dotenv

# Fix Windows console UTF-8 output encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH, override=True)

LOCAL_DB_PATH = os.path.join(BASE_DIR, "ghl_chroma_db")
DEFAULT_GEMINI_KEY = os.getenv("GEMINI_API_KEY", "").strip()

app = FastAPI(
    title="Python RAG Microservice for Laravel",
    description="Vector Search (5,379 Chunks) & Gemini Synthesis Engine for PHP Laravel",
    version="1.0.0"
)

client_chroma = None
collection = None
embed_model = None

def get_chroma_collection():
    global client_chroma, collection
    if collection is None:
        print("📦 [Microservice] Connecting to Local ChromaDB...")
        client_chroma = chromadb.PersistentClient(path=LOCAL_DB_PATH)
        collection = client_chroma.get_collection(name="ghl_knowledge_base")
        print(f"✅ [Microservice] ChromaDB collection loaded. Chunks: {collection.count()}")
    return collection

def get_embedding_model():
    global embed_model
    if embed_model is None:
        try:
            from fastembed import TextEmbedding
            print("🚀 [Microservice] Loading FastEmbed (nomic-ai/nomic-embed-text-v1.5) ONNX...")
            embed_model = TextEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5")
            print("✅ [Microservice] FastEmbed ONNX model ready!")
        except Exception as e_fe:
            print(f"ℹ️ FastEmbed fallback: {e_fe}")
            try:
                from sentence_transformers import SentenceTransformer
                embed_model = SentenceTransformer('nomic-ai/nomic-embed-text-v1.5', trust_remote_code=True)
                print("✅ [Microservice] SentenceTransformer model ready!")
            except Exception as e_st:
                print(f"❌ Could not load embedding model: {e_st}")
                embed_model = None
    return embed_model

class RAGSearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 4
    api_key: Optional[str] = None

class RAGSearchResponse(BaseModel):
    answer: str
    sources: List[str]
    query_time_ms: float
    top_k: int
    model: str = "gemini-3.5-flash"

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "python-rag-microservice",
        "chunks": 5379,
        "embedding_model": "nomic-embed-text-v1.5",
        "llm_model": "gemini-3.5-flash"
    }

@app.post("/api/rag-search", response_model=RAGSearchResponse)
async def rag_search_endpoint(req: RAGSearchRequest):
    user_query = req.query.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="Query string cannot be empty.")

    api_key = (req.api_key or "").strip() or DEFAULT_GEMINI_KEY

    start_time = time.time()
    try:
        col = get_chroma_collection()
        model = get_embedding_model()

        # 1. Vector Search
        # Detect simple greetings/pleasantries to optimize latency
        clean_query = user_query.strip().lower().rstrip('.!?')
        is_greeting = clean_query in {
            "hi", "hello", "hey", "hey there", "hello there", "greetings",
            "good morning", "good afternoon", "good evening", "good day",
            "aoa", "assalam o alaikum", "assalam-o-alaikum", "assalamu alaikum", "salam", "slaam",
            "how are you", "how are you?", "how r u", "who are you", "who are you?",
            "what can you do", "what can you do?", "help", "help me"
        }

        top_k = max(1, min(req.top_k or 4, 10))
        retrieved_docs = []
        if not is_greeting and col and model:
            if hasattr(model, 'embed'):
                embs = list(model.embed([f"search_query: {user_query}"]))
                query_emb = embs[0].tolist() if hasattr(embs[0], 'tolist') else list(embs[0])
            else:
                query_emb = model.encode(f"search_query: {user_query}").tolist()
            results = col.query(query_embeddings=[query_emb], n_results=top_k)
            retrieved_docs = results['documents'][0] if results and results.get('documents') else []

        context_str = "\n\n---\n\n".join(retrieved_docs) if retrieved_docs else "Standard GoHighLevel Knowledge Base."

        # 2. Executive System Prompt with Domain Guardrail & Greetings Policy
        prompt = f"""You are an elite GoHighLevel (GHL) Senior Technical Consultant & AI Assistant.
Synthesize an executive-level, highly professional response.

DOMAIN GUARDRAILS & GREETINGS POLICY:

1. GREETINGS & INTRODUCTIONS (NEVER TRIGGER OUT-OF-SCOPE ERROR):
- If the User Query is a greeting, pleasantry, conversational opener, or introductory question (e.g. "hi", "hello", "hey", "good morning", "assalam o alaikum", "who are you?", "how are you?", "can you help me?"):
- Respond warmly, courteously, and concisely.
- Greet the user back, introduce yourself as the GoHighLevel AI Technical Assistant, and invite them to ask any question regarding GoHighLevel (features, workflows, funnels, APIs, CRM settings, integrations, sub-accounts, or technical setups).
- DO NOT show an Out-of-Scope Notice or status banner for greetings.

2. STRICT OUT-OF-SCOPE POLICY (FOR NON-GHL OFF-TOPIC QUESTIONS ONLY):
- If the User Query asks a question about completely unrelated non-GHL topics (e.g. cooking, recipes, gaming, weather, sports, general politics, celebrities, movies, non-GHL trivia or homework):
- DO NOT answer the off-topic question.
- STRICTLY OUTPUT THE FOLLOWING EXECUTIVE NOTICE ONLY:

### ⚠️ Out-of-Scope Query Notice

I am an AI assistant specialized exclusively in **GoHighLevel (GHL) Technical Support & Workflow Automations**.

I am unable to answer queries outside the scope of GoHighLevel. Please feel free to ask any question regarding **GoHighLevel features, workflows, API integrations, funnels, CRM settings, or technical configurations**, and I will be glad to assist you!

3. GOHIGHLEVEL TECHNICAL QUERIES (Based on Documentation Context):
- For GHL technical questions, synthesize an answer based on the provided documentation context.
- Start with an executive status banner on the very first line:
  - Native feature: "### 🟢 Native GoHighLevel Feature"
  - Workaround required: "### 🟡 Workaround / Third-Party Integration Required"
  - General technical overview: "### ℹ️ GoHighLevel Technical Overview"
- Provide a clear, direct, and concise answer immediately below the banner.
- Match response length to the query: Keep simple questions short, crisp, and to the point.
- DO NOT append raw chunks, source excerpts, or related search document dumps to your reply text.
- If specific configuration is not present in context, state:
  "Information regarding this specific configuration is not available in the current GoHighLevel documentation."

Context:
{context_str}

User Query: {user_query}

Answer:"""

        # 3. Gemini Generation with primary model gemini-flash-latest
        client_gemini = genai.Client(api_key=api_key)
        try:
            response = client_gemini.models.generate_content(
                model='gemini-flash-latest',
                contents=prompt,
            )
            answer_text = response.text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Gemini API Error: {str(e)}")

        elapsed_ms = round((time.time() - start_time) * 1000, 2)

        return RAGSearchResponse(
            answer=answer_text,
            sources=[],
            query_time_ms=elapsed_ms,
            top_k=top_k,
            model="gemini-flash-latest"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("🚀 [Microservice] Starting Python RAG Engine for Laravel on http://127.0.0.1:7861 ...")
    uvicorn.run(app, host="127.0.0.1", port=7861)
