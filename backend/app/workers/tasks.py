from pathlib import Path
from app.core.config import get_settings
from app.processing.pipeline import process_lecture

def process_lecture_task(video_path: str, lecture_id: int) -> dict:
    work_dir=str(Path(get_settings().storage_dir)/str(lecture_id)/"processed")
    return process_lecture(video_path,work_dir)
