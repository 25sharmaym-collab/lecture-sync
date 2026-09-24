from pathlib import Path
import subprocess

def render_pdf(pdf_path: str, output_dir: str) -> list[str]:
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    prefix=str(out/"slide")
    subprocess.run(["pdftoppm","-jpeg","-r","96",pdf_path,prefix],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    return [str(p) for p in sorted(out.glob("slide-*.jpg"))]
