# Development Plan

## Milestones

0. Technical risk review
1. Repository + development environment
2. Database + models
3. Authentication + lecture CRUD
4. File upload
5. FFmpeg media pipeline
6. Whisper transcription
7. Slide extraction
8. Slide detection
9. Transcript-slide alignment
10. Lecture viewer
11. Search
12. Grounded AI
13. Notes + quizzes
14. Failure recovery
15. Testing
16. Benchmarking
17. Production Docker build
18. Deployment
19. Documentation + resume packaging

## Milestone 1 success criteria

- Repository contains a documented architecture.
- Docker Compose defines PostgreSQL and Redis.
- Environment template exists.
- No secrets are committed.
- Base project can be extended without restructuring.

## Working rule

Implement one verified milestone at a time. Expensive or failure-prone media operations must run outside HTTP request handlers.


## Milestone 1B — Frontend ↔ Backend

The Next.js frontend reads `NEXT_PUBLIC_API_URL` and calls the FastAPI `/health` endpoint.

Run the backend:
```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

Run the frontend in another terminal:
```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`. The page should report that the LectureSync API is healthy.

For local browser development, FastAPI allows requests from `http://localhost:3000`.
