import os
import sys
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Set up module path for Vercel Python Serverless runtime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

app = FastAPI(title="XortLogix High Level Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "XortLogix High Level Assistant",
        "runtime": "Vercel Serverless Python 3.12"
    }

# Lazy loading of main application to guarantee zero cold-start crashes
_main_app = None

def get_main_app():
    global _main_app
    if _main_app is None:
        from app import app as loaded_app
        _main_app = loaded_app
    return _main_app

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"])
async def dispatch_to_main_app(request: Request, full_path: str):
    # Direct fast-path for health
    if full_path in ["health", "api/health"]:
        return JSONResponse({"status": "healthy", "service": "XortLogix High Level Assistant"})

    try:
        main = get_main_app()
        return await main(request.scope, request.receive, request._send)
    except Exception as e:
        tb = traceback.format_exc()
        print("Dispatch error:", tb)
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": f"Serverless execution error: {str(e)}",
                "traceback": tb.splitlines()
            }
        )
