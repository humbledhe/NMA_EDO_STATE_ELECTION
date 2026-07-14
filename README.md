# NMA Edo State Election System

A secure web-based election platform for the **Nigerian Medical Association (NMA), Edo State Branch**.

The application enables verified members to register, authenticate, participate in elections, and view election results through a modern web interface.

## Status

🚧 **Under Active Development**

### Progress

- ✅ Project setup
- ✅ PostgreSQL database design
- ✅ User registration
- ✅ JWT authentication
- ✅ Password hashing
- 🚧 Landing page (in progress)
- 🚧 Live results dashboard (in progress)
- 🚧 Candidate management
- 🚧 Voting system
- ⏳ Real-time results
- ⏳ Admin dashboard

## Tech Stack

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)

### Frontend
- React
- Tailwind CSS
- React Router

## Getting Started

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## License

This project is proprietary software developed for the **Nigerian Medical Association (NMA), Edo State Branch**. All rights reserved.
