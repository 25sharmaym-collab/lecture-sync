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
