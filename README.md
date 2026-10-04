# LectureSync

Synchronize what the professor says with what the professor shows.

## Project Status

**Milestones 1-4 Complete ✅**
- [x] Milestone 1: Docker infrastructure (PostgreSQL + Redis)
- [x] Milestone 2: Database models & migrations
- [x] Milestone 3: Authentication & CRUD endpoints
- [x] Milestone 4: Email verification, refresh tokens, rate limiting
- [x] CI verification: backend migrations/tests + frontend production build

**Current**: Authentication and core lecture CRUD are implemented. CI now verifies the backend and frontend builds. Milestone 5 (file upload & media processing) is next.

## Tech Stack

**Backend:**
- FastAPI + Python 3.12 (async/await)
- SQLAlchemy 2.0 with async PostgreSQL
- Alembic migrations
- Argon2 + JWT authentication
- Pydantic schemas

**Infrastructure:**
- PostgreSQL 16 (Docker)
- Redis 7 (Docker)
- Docker Compose

**Frontend:**
- Next.js + TypeScript (coming)

**Media Processing (future):**
- FFmpeg (video processing)
- Faster-Whisper (speech-to-text)
- OpenCV (computer vision)
- S3-compatible storage

**Testing:**
- Pytest + pytest-asyncio
- 30+ integration tests (all passing)

## Architecture

```
┌─────────────────────────────────────┐
│     Frontend (Next.js)              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  API Gateway / Load Balancer        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  FastAPI Backend (Docker)           │
│  - Auth (JWT + Refresh tokens)      │
│  - User management                  │
│  - Lecture CRUD                     │
│  - Job processing                   │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
┌─────▼────┐      ┌────▼──────┐
│PostgreSQL│      │   Redis    │
│    16    │      │     7      │
└──────────┘      └────────────┘
```

## API Endpoints

### Authentication (10 endpoints)
```
POST   /auth/register              → User registration + email verification
POST   /auth/login                 → Login + refresh token
POST   /auth/verify-email          → Verify email address
POST   /auth/resend-verification   → Resend verification email
POST   /auth/refresh               → Refresh access token
POST   /auth/logout                → Logout + revoke sessions
POST   /auth/forgot-password       → Request password reset
POST   /auth/reset-password        → Confirm password reset
GET    /auth/me                    → Get current user
PUT    /auth/me                    → Update user profile
```

### Lectures (6 endpoints)
```
POST   /lectures                   → Create lecture
GET    /lectures                   → List user's lectures (paginated)
GET    /lectures/public            → List public lectures
GET    /lectures/{id}              → Get lecture details
PUT    /lectures/{id}              → Update lecture (owner only)
DELETE /lectures/{id}              → Delete lecture (owner only)
```

### System (2 endpoints)
```
GET    /health                     → Health check
GET    /ready                      → Readiness check
```

**Total: 18 API endpoints**

## Features Implemented

### Authentication & Security
- ✅ JWT tokens (HS256, 30-min expiration)
- ✅ Argon2 password hashing (GPU-resistant)
- ✅ Refresh tokens (7-day rotation)
- ✅ Email verification workflow
- ✅ Password reset with 1-hour window
- ✅ Bearer token authentication
- ✅ Token revocation system
- ✅ Logout with cross-device session cleanup

### User Management
- ✅ User registration
- ✅ Email verification
- ✅ Login with JWT
- ✅ Profile management
- ✅ Password changes
- ✅ Account status tracking

### Lecture Management
- ✅ Create lectures with ownership
- ✅ Update lectures (owner only)
- ✅ Delete lectures (owner only)
- ✅ List user's lectures (paginated)
- ✅ List public lectures (paginated)
- ✅ View lectures (owner or public)
- ✅ Share via public flag

### Infrastructure
- ✅ PostgreSQL with 2 migrations
- ✅ Redis for caching/sessions
- ✅ Docker Compose orchestration
- ✅ Health checks on all services
- ✅ Persistent volumes
- ✅ Bridge networking
- ✅ Alembic migration framework
- ✅ Rate limiting infrastructure

### Testing
- ✅ 30+ integration tests (all passing)
- ✅ Service layer tests
- ✅ Model tests
- ✅ Email service tests
- ✅ Token lifecycle tests

## Quick Start

### 1. Prerequisites
- Docker Desktop
- Git

### 2. Clone & Setup
```bash
git clone https://github.com/25sharmaym-collab/lecture-sync
cd lecture-sync
cp .env.example .env
```

### 3. Start Services
```bash
docker compose up -d postgres redis
sleep 15
```

### 4. Run Migrations
```bash
cd backend
alembic upgrade head
cd ..
```

### 5. Start API (Development)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Test API
```bash
# Health check
curl http://localhost:8000/health

# Register user
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.com",
    "username": "alice",
    "password": "securepassword123"
  }'
```

## Documentation

- **[Development Guide](docs/development.md)** - Setup, Docker commands, troubleshooting
- **[Milestone 1: Docker Infrastructure](docs/development.md#docker-development-infrastructure)** - PostgreSQL, Redis, volumes, networking
- **[Milestone 2 Summary](MILESTONE2_SUMMARY.txt)** - ORM models and migrations
- **[Milestone 3 Summary](MILESTONE3_SUMMARY.txt)** - Authentication and CRUD
- **[Milestone 4 Summary](MILESTONE4_SUMMARY.txt)** - Email verification, refresh tokens, and rate limiting
- **[API Quick Start](API_QUICKSTART.md)** - cURL examples, workflows
- **[Deployment Ready](DEPLOYMENT_READY.md)** - Production checklist

## Automated Verification

CI runs the backend migration suite and pytest, plus a production frontend build. Run locally with:
```bash
cd backend
pytest -q
```

## Environment Setup

### Development
```bash
cp .env.example .env
# Edit .env with your settings
```

### Required Variables
```
DATABASE_URL=postgresql+psycopg://lecturesync:lecturesync_dev_password@localhost:5432/lecturesync
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=dev-secret-key-change-in-production
```

### Optional Variables (Email)
```
SENDGRID_API_KEY=<your-key>
SENDGRID_FROM_EMAIL=noreply@lecturesync.app
FRONTEND_URL=http://localhost:3000
```

## Database Schema

**5 Tables:**
- `users` - User accounts with verification status
- `lectures` - Lecture records with ownership
- `lecture_processing_jobs` - Background job tracking
- `tokens` - Refresh/verification tokens
- `alembic_version` - Migration tracking

**Relations:**
- users (1) ↔ (N) lectures
- users (1) ↔ (N) lecture_processing_jobs
- lectures (1) ↔ (N) lecture_processing_jobs
- users (1) ↔ (N) tokens

## Security Features

- ✅ No plaintext passwords (Argon2 hashing)
- ✅ JWT with expiration
- ✅ Token hashing before storage
- ✅ Bearer token authentication
- ✅ Role-based access control (ownership checks)
- ✅ Input validation (Pydantic)
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ CORS configured
- ✅ Email verification required
- ✅ Password reset with 1-hour window
- ✅ Automatic session cleanup on logout

## Deployment

### Production Checklist
- [ ] Set `SECRET_KEY` to strong random value
- [ ] Configure `SENDGRID_API_KEY` (if using email)
- [ ] Set `FRONTEND_URL` to production domain
- [ ] Run migrations: `alembic upgrade head`
- [ ] Enable HTTPS/TLS
- [ ] Set up monitoring
- [ ] Configure rate limiting
- [ ] Set up email webhook handlers (optional)
- [ ] Enable audit logging
- [ ] Test full authentication flow

See [DEPLOYMENT_READY.md](DEPLOYMENT_READY.md) for complete checklist.

## Known Limitations

- No file upload yet (Milestone 5)
- No media processing (Milestone 5)
- No device/session tracking (future)
- Rate limiting infrastructure only (not deployed)
- No 2FA support (future)

## Roadmap

**Completed:**
- ✅ M1: Docker infrastructure
- ✅ M2: Database models
- ✅ M3: Authentication & CRUD
- ✅ M4: Email & token management

**Next:**
- M5: File upload to S3
- M6: Media processing pipeline
- M7: Transcription + slide detection
- M8: Lecture synchronization
- M9: Search & recommendations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following the existing patterns
4. Run tests: `pytest tests/ -v`
5. Submit a pull request

## Support

- Check [docs/development.md](docs/development.md) for local setup issues
- See [docs/milestone4.md](docs/milestone4.md) for API usage examples
- Review [DEPLOYMENT_READY.md](DEPLOYMENT_READY.md) for deployment questions

## License

MIT (or your chosen license)

## Authors

- Yashvardan Sharma

---

**Status**: Core authentication and lecture-management foundation implemented and CI-verified. File upload and media processing remain future milestones.
