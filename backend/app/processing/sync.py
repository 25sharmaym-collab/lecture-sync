from bisect import bisect_right

def transcript_slide_context(transcript:list[dict], intervals:list[dict])->list[dict]:
    starts=[float(x["start"]) for x in intervals]
    out=[]
    for seg in transcript:
        t=float(seg["start"])
        i=bisect_right(starts,t)-1
        slide=intervals[i]["slide_index"] if i>=0 else None
        out.append({**seg,"slide_index":slide})
    return out
