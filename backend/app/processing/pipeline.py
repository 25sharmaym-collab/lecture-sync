from pathlib import Path
from app.processing.media import extract_audio
from app.processing.transcription import transcribe,to_dicts
from app.processing.pdf import render_slides
from app.processing.slide_match import match_slides
from app.processing.sync import transcript_slide_context
from app.processing.artifacts import write_json,write_vtt

def process_lecture(video_path:str,slides_path:str|None,work_dir:str,whisper_model:str="small")->dict:
    root=Path(work_dir); root.mkdir(parents=True,exist_ok=True)
    audio=str(root/"audio.wav"); extract_audio(video_path,audio)
    transcript=to_dicts(transcribe(audio,whisper_model))
    slides=[]
    intervals=[]
    if slides_path:
        slides=render_slides(slides_path,str(root/"slides"))
        raw=match_slides(video_path,slides)
        intervals=[{"slide_index":x.slide_index+1,"start":x.start,"end":x.end} for x in raw]
    synced=transcript_slide_context(transcript,intervals) if intervals else transcript
    transcript_path=write_json(str(root/"transcript.json"),synced)
    vtt_path=write_vtt(str(root/"transcript.vtt"),synced)
    timeline_path=write_json(str(root/"timeline.json"),{"slides":intervals,"transcript":synced})
    return {"transcript":synced,"slides":slides,"slide_intervals":intervals,"transcript_path":transcript_path,"vtt_path":vtt_path,"timeline_path":timeline_path}
