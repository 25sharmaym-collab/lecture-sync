# LectureSync API - Quick Start Guide

## Start Services

```bash
docker compose up -d postgres redis
sleep 15
```

## Install Dependencies

```bash
cd backend
pip install -r requirements.txt
cd ..
```

## Run Migrations

```bash
cd backend
alembic upgrade head
cd ..
```

## Run Tests

```bash
cd backend
pytest tests/test_services.py -v
cd ..
```

## Start API Server

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: http://localhost:8000

## API Endpoints

### Health Checks
```
GET /health
GET /ready
```

### Authentication
```
POST /auth/register
  {
    "email": "user@example.com",
    "username": "john",
    "password": "password123"
  }

POST /auth/login
  {
    "email": "user@example.com",
    "password": "password123"
  }

GET /auth/me
  Headers: Authorization: Bearer <token>

PUT /auth/me
  Headers: Authorization: Bearer <token>
  {
    "username": "new_username"
  }
```

### Lectures
```
POST /lectures
  Headers: Authorization: Bearer <token>
  {
    "title": "My Lecture",
    "description": "Description here",
    "video_filename": "lecture.mp4",
    "is_public": false
  }

GET /lectures
  Headers: Authorization: Bearer <token>

GET /lectures/public

GET /lectures/{id}
  Headers: Authorization: Bearer <token>

PUT /lectures/{id}
  Headers: Authorization: Bearer <token>
  {
    "title": "New Title",
    "is_public": true
  }

DELETE /lectures/{id}
  Headers: Authorization: Bearer <token>
```

## Example Workflow

### 1. Register User
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.com",
    "username": "alice",
    "password": "securepassword123"
  }'
```

Copy the `access_token` from response.

### 2. Login
```bash
TOKEN="<access_token_from_above>"

curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.com",
    "password": "securepassword123"
  }'
```

### 3. Get Profile
```bash
curl -X GET http://localhost:8000/auth/me \
  -H "Authorization: Bearer $TOKEN"
```

### 4. Create Lecture
```bash
curl -X POST http://localhost:8000/lectures \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python Fundamentals",
    "description": "Learn Python basics",
    "video_filename": "python_101.mp4",
    "is_public": false
  }'
```

Copy the `id` from response.

### 5. List Your Lectures
```bash
curl -X GET http://localhost:8000/lectures \
  -H "Authorization: Bearer $TOKEN"
```

### 6. Get Lecture Details
```bash
LECTURE_ID="<id_from_above>"

curl -X GET http://localhost:8000/lectures/$LECTURE_ID \
  -H "Authorization: Bearer $TOKEN"
```

### 7. Update Lecture
```bash
curl -X PUT http://localhost:8000/lectures/$LECTURE_ID \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Advanced Python",
    "is_public": true
  }'
```

### 8. Delete Lecture
```bash
curl -X DELETE http://localhost:8000/lectures/$LECTURE_ID \
  -H "Authorization: Bearer $TOKEN"
```

## OpenAPI Documentation

Once API is running, visit:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

## Environment Variables

Create a `.env` file in the backend directory:

```
DATABASE_URL=postgresql+psycopg://lecturesync:lecturesync_dev_password@localhost:5432/lecturesync
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=dev-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Status Codes

- `200` - Success
- `201` - Created
- `204` - No Content (successful delete)
- `400` - Bad Request (validation error)
- `401` - Unauthorized (missing/invalid token)
- `403` - Forbidden (no permission)
- `404` - Not Found

## Troubleshooting

### "Cannot connect to database"
```bash
docker compose up -d postgres
docker compose ps
```

### "Invalid or expired token"
- Token expired after 30 minutes → Get new token via login
- Wrong SECRET_KEY → Check .env file
- Malformed token → Ensure "Bearer " prefix in header

### "Email already registered"
```bash
# Use a different email or login
curl -X POST http://localhost:8000/auth/login ...
```

### Tests failing
```bash
cd backend
# Ensure DB is running
docker compose up -d postgres

# Run migrations
alembic upgrade head

# Run tests
pytest tests/test_services.py -v
```

## Performance

- Token generation: < 1ms
- Password hash verification: ~100ms (intentionally slow for security)
- Database queries: Indexed for fast lookups
- Pagination: Default 20 items per page, max 100

## Security Notes

- Passwords are hashed with Argon2 (never stored plaintext)
- Tokens expire after 30 minutes
- Only change SECRET_KEY when rotting all tokens
- Use HTTPS in production
- Consider rate limiting for production

## Next Steps

See `docs/milestone3.md` for complete API documentation.

