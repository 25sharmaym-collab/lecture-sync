from pathlib import Path
import subprocess

def run(*args: str) -> None:
    subprocess.run(list(args), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def extract_audio(video_path: str, out_path: str) -> str:
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    run("ffmpeg","-y","-i",video_path,"-vn","-ac","1","-ar","16000","-c:a","pcm_s16le",out_path)
    return out_path
