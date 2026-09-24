from dataclasses import dataclass
from pathlib import Path
import cv2
import numpy as np

@dataclass
class SlideInterval:
    slide_index:int
    start:float
    end:float

def image_signature(path:str)->np.ndarray:
    image=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    if image is None: raise ValueError(f"Cannot read slide image: {path}")
    return cv2.resize(image,(32,18)).astype(np.float32)/255.0

def frame_signature(cap,second:float)->np.ndarray|None:
    cap.set(cv2.CAP_PROP_POS_MSEC,second*1000)
    ok,frame=cap.read()
    if not ok:return None
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    return cv2.resize(gray,(32,18)).astype(np.float32)/255.0

def match_slides(video_path:str,slide_images:list[str],sample_seconds:float=2.0,threshold:float=0.88)->list[SlideInterval]:
    if not slide_images:return []
    refs=[image_signature(p) for p in slide_images]
    cap=cv2.VideoCapture(video_path)
    if not cap.isOpened(): raise ValueError("Cannot open video")
    duration=(cap.get(cv2.CAP_PROP_FRAME_COUNT)/max(cap.get(cv2.CAP_PROP_FPS),1.0))
    samples=[]
    t=0.0
    while t<=duration:
        sig=frame_signature(cap,t)
        if sig is not None:
            scores=[1.0-float(np.mean((sig-r)**2)) for r in refs]
            idx=int(np.argmax(scores))
            if scores[idx]>=threshold:samples.append((t,idx))
        t+=sample_seconds
    cap.release()
    if not samples:return []
    intervals=[]; current=samples[0][1]; start=samples[0][0]
    for t,idx in samples[1:]:
        if idx!=current:
            intervals.append(SlideInterval(current,start,t))
            current=idx; start=t
    intervals.append(SlideInterval(current,start,duration))
    return intervals
