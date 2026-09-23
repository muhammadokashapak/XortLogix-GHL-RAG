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

try:
    from app import app
except Exception as e:
    tb = traceback.format_exc()
    print("FATAL STARTUP ERROR IN APP.PY:", tb)
    app = FastAPI(title="XortLogix High Level Assistant (Fallback)")
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    @app.get("/api/health")
    async def health():
        return {
            "status": "degraded",
            "service": "XortLogix High Level Assistant",
            "error": str(e),
            "traceback": tb.splitlines()
        }

    @app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"])
    async def catch_all_error(full_path: str):
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "FastAPI initialization failed on Vercel",
                "exception": str(e),
                "traceback": tb.splitlines()
            }
        )

# Direct fallback route handlers on app for explicit health/status
@app.get("/api/index.py")
@app.get("/api/index")
@app.get("/api")
async def root_api_status():
    return {
        "status": "online",
        "service": "XortLogix High Level Assistant",
        "runtime": "Vercel Python 3.12 Serverless"
    }
