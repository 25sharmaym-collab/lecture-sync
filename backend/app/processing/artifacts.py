from pathlib import Path
import json

def write_json(path:str,data)->str:
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8"); return str(p)

def write_vtt(path:str,segments:list[dict])->str:
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    def ts(v:float)->str:
        ms=int(round(v*1000)); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000); return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
    lines=["WEBVTT",""]
    for x in segments:
        lines += [f"{ts(float(x['start']))} --> {ts(float(x['end']))}",x["text"],""]
    p.write_text("\n".join(lines),encoding="utf-8"); return str(p)
