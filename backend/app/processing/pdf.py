from pathlib import Path

def render_slides(input_path:str,output_dir:str)->list[str]:
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    ext=Path(input_path).suffix.lower()
    if ext==".pdf":
        import fitz
        doc=fitz.open(input_path); paths=[]
        for i,page in enumerate(doc):
            pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
            p=out/f"slide-{i+1:04d}.jpg"; pix.save(str(p)); paths.append(str(p))
        doc.close(); return paths
    if ext==".pptx":
        raise RuntimeError("PPTX rendering requires LibreOffice in the processing image")
    raise ValueError("Unsupported slide format")
