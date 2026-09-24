from pathlib import Path
from app.processing.media import extract_audio
from app.processing.transcription import transcribe,to_dicts

def process_lecture(video_path: str, work_dir: str, whisper_model: str = "small") -> dict:
    root=Path(work_dir); root.mkdir(parents=True,exist_ok=True)
    audio=str(root/"audio.wav")
    extract_audio(video_path,audio)
    transcript=to_dicts(transcribe(audio,whisper_model))
    (root/"transcript.json").write_text(__import__("json").dumps(transcript,ensure_ascii=False,indent=2),encoding="utf-8")
    return {"audio_path":audio,"transcript_path":str(root/"transcript.json"),"transcript":transcript}
