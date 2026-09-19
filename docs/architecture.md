# LectureSync Architecture

## Core principle

The deterministic lecture pipeline comes first:

Video → audio extraction → timestamped transcription

Slides → normalized images → slide detection → slide intervals

Then:

transcript timestamps + slide intervals → synchronized lecture

AI is a later layer over verified lecture data.

## MVP components

### Frontend
Next.js + TypeScript.

### API
FastAPI for HTTP APIs and later WebSocket endpoints.

### Persistence
PostgreSQL for application and temporal lecture data.

### Background work
Redis-backed queue/worker architecture for expensive media processing.

### Media
FFmpeg for media inspection and audio extraction.

### Speech
faster-whisper for timestamped transcription.

### Slides
PyMuPDF for PDF rendering/extraction. PPTX support will be added with a reliable rendering path.

### Computer vision
OpenCV-based frame sampling and slide matching. Accuracy will be benchmarked rather than assumed.

## Important constraint

Do not introduce Elasticsearch, Kafka, Kubernetes, vector databases, or microservices unless measured requirements justify them.
