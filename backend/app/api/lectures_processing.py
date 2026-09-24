from pathlib import Path
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.core.db import get_db
from app.models.lecture import Lecture
from app.models.user import User
from app.schemas.processing import TranscriptResponse,TranscriptSegmentResponse
from app.workers.tasks import process_lecture_task

router=APIRouter(prefix="/lectures",tags=["processing"])

@router.post("/{lecture_id}/process/transcript",response_model=TranscriptResponse)
async def transcript(lecture_id:int,u:User=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    x=await db.get(Lecture,lecture_id)
    if not x or x.owner_id!=u.id: raise HTTPException(404,"Lecture not found")
    if not x.video_path: raise HTTPException(400,"Upload a video first")
    x.status="processing"; x.processing_error=None; await db.commit()
    try:
        result=process_lecture_task(x.video_path,x.id)
        x.status="ready"; await db.commit()
        return TranscriptResponse(lecture_id=x.id,segments=[TranscriptSegmentResponse(**s) for s in result["transcript"]])
    except Exception as exc:
        x.status="failed"; x.processing_error=str(exc)[:2000]; await db.commit()
        raise HTTPException(500,"Media processing failed") from exc
