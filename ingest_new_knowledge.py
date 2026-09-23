"""
GoHighLevel (GHL) Knowledge Ingestion & Vector Embedding Pipeline
==================================================================
This script:
1. Loads scraped API/OAuth docs from `scraped_ghl_docs/` and `ghl_api_oauth_and_custom_dev_knowledge.md`.
2. Chunks documents semantically preserving headings, code snippets, and metadata.
3. Generates vector embeddings using FastEmbed ONNX (or SentenceTransformers fallback) with `nomic-ai/nomic-embed-text-v1.5`.
4. Upserts all chunks into the local ChromaDB vector database (`ghl_chroma_db/ghl_knowledge_base`).
"""

import os
import re
import sys
import gc
import json
import time
import hashlib
from typing import List, Dict, Any, Tuple
import chromadb

# Ensure UTF-8 output on Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Directories and Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "ghl_chroma_db")
COLLECTION_NAME = "ghl_knowledge_base"

SCRAPED_DIR = os.path.join(BASE_DIR, "scraped_ghl_docs")
SCRAPED_JSON_FILE = os.path.join(SCRAPED_DIR, "ghl_api_scraped_data.json")
CUSTOM_DEV_MD_FILE = os.path.join(BASE_DIR, "ghl_api_oauth_and_custom_dev_knowledge.md")

BATCH_SIZE = 16  # Safe batch size for fast & memory-safe execution


def get_embedding_model():
    """Loads FastEmbed ONNX or fallback SentenceTransformers."""
    try:
        from fastembed import TextEmbedding
        print("🚀 Loading FastEmbed (nomic-ai/nomic-embed-text-v1.5) ONNX...", flush=True)
        embed_model = TextEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5", threads=1)
        print("✅ FastEmbed ONNX model ready!", flush=True)
        return embed_model, "fastembed"
    except Exception as e_fe:
        print(f"ℹ️ FastEmbed note: {e_fe}. Trying SentenceTransformers...", flush=True)

    try:
        from sentence_transformers import SentenceTransformer
        print("🔄 Loading SentenceTransformer (nomic-ai/nomic-embed-text-v1.5)...", flush=True)
        embed_model = SentenceTransformer('nomic-ai/nomic-embed-text-v1.5', trust_remote_code=True)
        print("✅ SentenceTransformer model ready!", flush=True)
        return embed_model, "sentence_transformers"
    except Exception as e:
        print(f"❌ Failed to load embedding model: {e}", flush=True)
        return None, None


def split_text_into_chunks(text: str, chunk_size_words: int = 300, overlap_words: int = 40) -> List[str]:
    """Splits a document text into overlapping word-bounded chunks."""
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = []
    current_count = 0

    for para in paragraphs:
        para_clean = para.strip()
        if not para_clean:
            continue
        
        words = para_clean.split()
        word_count = len(words)

        if current_count + word_count <= chunk_size_words:
            current_chunk.append(para_clean)
            current_count += word_count
        else:
            if current_chunk:
                chunks.append("\n\n".join(current_chunk))
            
            # Start new chunk
            if word_count > chunk_size_words:
                for i in range(0, word_count, chunk_size_words - overlap_words):
                    sub_words = words[i:i + chunk_size_words]
                    chunks.append(" ".join(sub_words))
                current_chunk = []
                current_count = 0
            else:
                current_chunk = [para_clean]
                current_count = word_count

    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    return [c.strip() for c in chunks if len(c.strip()) > 60]


def prepare_all_documents() -> List[Dict[str, Any]]:
    """Loads and chunks all source documents."""
    all_chunks: List[Dict[str, Any]] = []

    # 1. Process Custom Dev & Native Workarounds File
    if os.path.exists(CUSTOM_DEV_MD_FILE):
        print(f"📄 Processing Custom Dev Guide: {CUSTOM_DEV_MD_FILE}...", flush=True)
        with open(CUSTOM_DEV_MD_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        sections = re.split(r'\n(?=##\s+)', content)
        for sec in sections:
            if not sec.strip():
                continue
            title_match = re.search(r'##\s+(.+)', sec)
            section_title = title_match.group(1).strip() if title_match else "Custom GHL Solutions"
            
            sec_chunks = split_text_into_chunks(sec, chunk_size_words=250, overlap_words=30)
            for c_idx, chunk_text in enumerate(sec_chunks):
                chunk_id = hashlib.md5(f"custom_dev_{section_title}_{c_idx}_{chunk_text[:50]}".encode('utf-8')).hexdigest()
                all_chunks.append({
                    "id": chunk_id,
                    "text": chunk_text,
                    "title": f"Custom Dev: {section_title}",
                    "source": "GoHighLevel Custom Dev & Frontend Blueprint",
                    "category": "custom_development_and_frontend"
                })

    # 2. Process Scraped API Documentation
    if os.path.exists(SCRAPED_JSON_FILE):
        print(f"📄 Processing Scraped API Documentation Index: {SCRAPED_JSON_FILE}...", flush=True)
        with open(SCRAPED_JSON_FILE, "r", encoding="utf-8") as f:
            scraped_items = json.load(f)

        for item in scraped_items:
            title = item.get("title", "GHL API Doc")
            url = item.get("url", "https://marketplace.gohighlevel.com/docs/")
            raw_md = item.get("markdown", "")

            if not raw_md or len(raw_md.strip()) < 80:
                continue

            doc_chunks = split_text_into_chunks(raw_md, chunk_size_words=300, overlap_words=40)
            for c_idx, chunk_text in enumerate(doc_chunks):
                chunk_id = hashlib.md5(f"scraped_{title}_{c_idx}_{chunk_text[:50]}".encode('utf-8')).hexdigest()
                all_chunks.append({
                    "id": chunk_id,
                    "text": chunk_text,
                    "title": title,
                    "source": url,
                    "category": "ghl_rest_api_and_oauth"
                })

    print(f"📊 Total Structured Knowledge Chunks Prepared: {len(all_chunks)}", flush=True)
    return all_chunks


def run_ingestion():
    """Main runner to embed and save into ChromaDB."""
    print("=" * 70, flush=True)
    print("🚀 GHL RAG KNOWLEDGE INGESTION PIPELINE", flush=True)
    print("=" * 70, flush=True)

    # 1. Prepare Chunks
    chunks = prepare_all_documents()
    if not chunks:
        print("❌ No chunks found to ingest. Please make sure files exist.", flush=True)
        return

    # 2. Load Embedding Model
    embed_model, embed_type = get_embedding_model()
    if not embed_model:
        print("❌ Failed to initialize embedding engine.", flush=True)
        return

    # 3. Connect to ChromaDB
    print(f"\n📦 Connecting to ChromaDB at: {CHROMA_DB_PATH} ...", flush=True)
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    initial_count = collection.count()
    print(f"ℹ️ Current collection chunk count: {initial_count}", flush=True)

    # 4. Batch Embed and Upsert
    total_chunks = len(chunks)
    print(f"\n⚡ Ingesting {total_chunks} chunks in batches of {BATCH_SIZE}...", flush=True)
    start_time = time.time()

    for i in range(0, total_chunks, BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        batch_ids = [c["id"] for c in batch]
        batch_docs = [c["text"] for c in batch]
        batch_metadatas = [{
            "title": c["title"],
            "source": c["source"],
            "category": c["category"]
        } for c in batch]

        # Prepare inputs with safe length truncation for fast & low-RAM embedding
        batch_inputs = [f"search_document: {doc[:800].strip()}" for doc in batch_docs]

        # Generate Embeddings safely
        batch_embeddings = []
        if embed_type == "fastembed":
            try:
                embs = list(embed_model.embed(batch_inputs, batch_size=8))
                batch_embeddings = [e.tolist() if hasattr(e, 'tolist') else list(e) for e in embs]
            except Exception:
                for single_in in batch_inputs:
                    e_item = list(embed_model.embed([single_in[:400]], batch_size=1))[0]
                    batch_embeddings.append(e_item.tolist() if hasattr(e_item, 'tolist') else list(e_item))
        else:
            batch_embeddings = embed_model.encode(batch_inputs, batch_size=8).tolist()

        # Upsert into ChromaDB
        collection.upsert(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metadatas,
            embeddings=batch_embeddings
        )

        progress = min(i + BATCH_SIZE, total_chunks)
        percent = round((progress / total_chunks) * 100, 1)
        print(f"[{progress}/{total_chunks}] ({percent}%) 📥 Upserted batch into ChromaDB...", flush=True)

    # Final Stats
    final_count = collection.count()
    elapsed = round(time.time() - start_time, 2)
    gc.collect()

    print("\n" + "=" * 70, flush=True)
    print("🎉 INGESTION & EMBEDDING SUCCESSFULLY COMPLETED!", flush=True)
    print(f"⏱️ Time Elapsed: {elapsed} seconds", flush=True)
    print(f"📦 Initial Chunks: {initial_count}", flush=True)
    print(f"📈 Total Chunks in ChromaDB Now: {final_count} (+{final_count - initial_count} added)", flush=True)
    print(f"🗄️ Database Location: {CHROMA_DB_PATH}", flush=True)
    print("=" * 70, flush=True)

   
if __name__ == "__main__":
    run_ingestion()
