from dataclasses import dataclass
from typing import Any

@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str

def transcribe(audio_path: str, model_name: str = "small") -> list[TranscriptSegment]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError("Install faster-whisper to enable transcription") from exc
    model = WhisperModel(model_name, device="auto", compute_type="auto")
    segments, _ = model.transcribe(audio_path, vad_filter=True)
    return [TranscriptSegment(float(s.start),float(s.end),s.text.strip()) for s in segments if s.text.strip()]

def to_dicts(segments: list[TranscriptSegment]) -> list[dict[str, Any]]:
    return [{"start":s.start,"end":s.end,"text":s.text} for s in segments]
