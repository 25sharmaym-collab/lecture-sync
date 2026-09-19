# LectureSync

Synchronize what the professor says with what the professor shows.

## Project status

Milestone 1 — repository and development environment bootstrap.

## Planned stack

- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python
- Database: PostgreSQL
- Queue/cache: Redis
- Media: FFmpeg
- Speech-to-text: faster-whisper
- Computer vision: OpenCV
- Storage: S3-compatible object storage
- Tests: Pytest + Playwright

## MVP

1. Upload lecture video
2. Upload PDF slide deck
3. Process media
4. Generate timestamped transcript
5. Detect slide intervals
6. Align transcript to slides
7. Watch synchronized lecture
8. Search lecture content

See docs/architecture.md and docs/development.md for the current plan.

## Local development

Prerequisites: Docker Desktop, Git, Node.js 22+, Python 3.12+

```bash
cp .env.example .env
docker compose up --build
```
