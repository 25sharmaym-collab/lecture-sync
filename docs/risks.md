# Technical Risks

## Highest-risk areas

1. Slide detection accuracy when the lecturer occludes the screen, the recording is angled, or slides contain animation.
2. Whisper chunk boundary merging and timestamp correctness.
3. Long-running media processing and resource usage.
4. Storage and download cost for large recordings.
5. Maintaining synchronization without UI timer drift.
6. Grounding AI answers in exact transcript/slide evidence.

## Mitigation

- benchmark slide matching on representative recordings;
- store confidence and allow retries;
- keep deterministic processing independent from LLM availability;
- build idempotent stages;
- drive playback state from the HTML5 video's currentTime;
- measure actual processing time and memory before making performance claims.
