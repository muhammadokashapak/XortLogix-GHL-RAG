import os
import sys
import uvicorn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Check if app.py is directly here or inside 'GHL RAG'
if os.path.exists(os.path.join(BASE_DIR, "app.py")):
    sys.path.insert(0, BASE_DIR)
elif os.path.exists(os.path.join(BASE_DIR, "GHL RAG", "app.py")):
    ghl_path = os.path.join(BASE_DIR, "GHL RAG")
    os.chdir(ghl_path)
    sys.path.insert(0, ghl_path)

if __name__ == "__main__":
    port_str = os.getenv("PORT", "7860").strip()
    try:
        port = int(port_str)
    except ValueError:
        port = 7860

    host = "0.0.0.0"
    print(f"🚀 [Railway] Starting GoHighLevel RAG on {host}:{port} ...")
    uvicorn.run("app:app", host=host, port=port, log_level="info")
