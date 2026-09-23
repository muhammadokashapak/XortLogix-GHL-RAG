import os
import sys
import traceback

# Set up module path for Vercel Python Serverless runtime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from app import app
except Exception as e:
    tb = traceback.format_exc()
    print("FATAL STARTUP ERROR:", tb)
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI(title="Error Fallback")
    
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
