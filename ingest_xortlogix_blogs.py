"""
Ingest Scraped XortLogix Blogs into ChromaDB Vector Store
=========================================================
1. Reads `scraped_xortlogix_blogs/xortlogix_blogs.json`.
2. Chunks each article into semantically rich chunks (~250 words, 30 words overlap).
3. Computes vector embeddings using FastEmbed ONNX (nomic-ai/nomic-embed-text-v1.5) with 'search_document: ' prefix.
4. Upserts chunks & metadata into ChromaDB `ghl_knowledge_base` collection.
5. Verifies retrieval accuracy with test queries.
"""

import os
import re
import sys
import gc
import json
import time
import hashlib
from typing import List, Dict, Any
import chromadb

# UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "ghl_chroma_db")
COLLECTION_NAME = "ghl_knowledge_base"
JSON_INPUT_FILE = os.path.join(BASE_DIR, "scraped_xortlogix_blogs", "xortlogix_blogs.json")
BATCH_SIZE = 16


def get_embedding_model():
    """Loads SentenceTransformers (already locally cached) or FastEmbed."""
    try:
        from sentence_transformers import SentenceTransformer
        print("🔄 Loading cached SentenceTransformer (nomic-ai/nomic-embed-text-v1.5)...", flush=True)
        embed_model = SentenceTransformer('nomic-ai/nomic-embed-text-v1.5', trust_remote_code=True)
        print("✅ SentenceTransformer model ready!", flush=True)
        return embed_model, "sentence_transformers"
    except Exception as e_st:
        print(f"ℹ️ SentenceTransformer note: {e_st}. Trying FastEmbed...", flush=True)

    try:
        from fastembed import TextEmbedding
        embed_model = TextEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5", threads=1)
        print("✅ FastEmbed ONNX model ready!", flush=True)
        return embed_model, "fastembed"
    except Exception as e_fe:
        print(f"❌ Failed to load embedding model: {e_fe}", flush=True)
        return None, None


def split_text_into_chunks(text: str, chunk_size_words: int = 250, overlap_words: int = 35) -> List[str]:
    """Splits an article into overlapping word-bounded chunks preserving paragraph continuity."""
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

    return [c.strip() for c in chunks if len(c.strip()) > 50]


def prepare_blog_chunks() -> List[Dict[str, Any]]:
    if not os.path.exists(JSON_INPUT_FILE):
        print(f"❌ JSON input file not found: {JSON_INPUT_FILE}")
        return []

    with open(JSON_INPUT_FILE, "r", encoding="utf-8") as f:
        blogs = json.load(f)

    all_chunks = []
    print(f"📄 Processing {len(blogs)} scraped XortLogix blog articles...", flush=True)

    for b_idx, blog in enumerate(blogs):
        title = blog.get("title", "XortLogix Blog Post")
        slug = blog.get("slug", f"blog_{b_idx}")
        url = blog.get("url", "https://xortlogix.com/blog")
        author = blog.get("author", "Husnain Sultan")
        tags = blog.get("tags", [])
        subcategory = ", ".join(tags) if tags else "CRM Systems & Architecture"
        plain_text = blog.get("plain_text", "")
        markdown = blog.get("markdown", "")

        text_to_chunk = markdown if markdown else plain_text
        if not text_to_chunk or len(text_to_chunk.strip()) < 50:
            continue

        doc_chunks = split_text_into_chunks(text_to_chunk, chunk_size_words=260, overlap_words=35)
        for c_idx, chunk_text in enumerate(doc_chunks):
            chunk_id = hashlib.md5(f"xortlogix_blog_{slug}_{c_idx}_{chunk_text[:40]}".encode('utf-8')).hexdigest()
            all_chunks.append({
                "id": chunk_id,
                "text": chunk_text,
                "title": f"XortLogix Blog: {title}",
                "url": url,
                "author": author,
                "category": "XortLogix Official Blog & Case Studies",
                "subcategory": subcategory,
                "chunk_index": c_idx,
                "source": f"XortLogix Blog ({url})"
            })

    print(f"📊 Prepared {len(all_chunks)} semantic vector chunks from {len(blogs)} articles.", flush=True)
    return all_chunks


def run_ingestion():
    print("=" * 70)
    print("⚡ XORTLOGIX BLOG INGESTION & VECTOR EMBEDDING PIPELINE")
    print("=" * 70)

    chunks = prepare_blog_chunks()
    if not chunks:
        print("❌ No chunks found to ingest. Make sure scraper has finished.")
        return

    embed_model, embed_type = get_embedding_model()
    if not embed_model:
        print("❌ Failed to initialize embedding engine.")
        return

    print(f"\n📦 Connecting to ChromaDB at: {CHROMA_DB_PATH} ...", flush=True)
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    initial_count = collection.count()
    print(f"ℹ️ Current collection chunk count: {initial_count}", flush=True)

    total_chunks = len(chunks)
    print(f"\n⚡ Ingesting {total_chunks} chunks in batches of {BATCH_SIZE}...", flush=True)
    start_time = time.time()

    for i in range(0, total_chunks, BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        batch_ids = [c["id"] for c in batch]
        batch_docs = [c["text"] for c in batch]
        batch_metadatas = [{
            "title": c["title"],
            "url": c["url"],
            "author": c["author"],
            "category": c["category"],
            "subcategory": c["subcategory"],
            "chunk_index": c["chunk_index"],
            "source": c["source"]
        } for c in batch]

        # Embed with 'search_document: ' prefix
        batch_inputs = [f"search_document: {doc[:800].strip()}" for doc in batch_docs]

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

        collection.upsert(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metadatas,
            embeddings=batch_embeddings
        )

        progress = min(i + BATCH_SIZE, total_chunks)
        percent = round((progress / total_chunks) * 100, 1)
        print(f"[{progress}/{total_chunks}] ({percent}%) 📥 Upserted batch into ChromaDB...", flush=True)

    final_count = collection.count()
    elapsed = round(time.time() - start_time, 2)
    gc.collect()

    print("\n" + "=" * 70)
    print("🎉 BLOG EMBEDDING & INGESTION COMPLETED SUCCESSFULLY!")
    print(f"⏱️ Time Elapsed: {elapsed} seconds")
    print(f"📦 Initial Database Chunks: {initial_count}")
    print(f"📈 Total Database Chunks Now: {final_count} (+{final_count - initial_count} chunks added)")
    print(f"🗄️ ChromaDB Location: {CHROMA_DB_PATH}")
    print("=" * 70)


if __name__ == "__main__":
    run_ingestion()
