from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.api.lectures import router as lecture_router
from app.api.lectures_processing import router as processing_router
from app.core.config import get_settings
s=get_settings()
app=FastAPI(title="LectureSync API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=s.cors_origin_list,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(auth_router,prefix="/api/v1")
app.include_router(lecture_router,prefix="/api/v1")
app.include_router(processing_router,prefix="/api/v1")
@app.get("/health",tags=["system"])
async def health(): return {"status":"ok","service":"lecturesync-api"}
@app.get("/api/v1/health",tags=["system"])
async def api_health(): return {"status":"ok","service":"lecturesync-api"}
