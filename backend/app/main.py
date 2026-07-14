#Third Party
from fastapi import FastAPI
# Local modules
from app.users.route import router as users_route


app = FastAPI(
    title="NMA Edo State Election Platform API",
description="""
A secure and scalable REST API powering the NMA Edo State Election Platform.

This API provides the backend services required to manage election processes,
including voter authentication, candidate administration, secure vote submission,
and election result management.

## Core Features
- Secure user authentication and authorization (JWT)
- Role-based access control for administrators and voters
- Voter registration and verification
- Candidate management
- Election creation and configuration
- Secure vote casting and validation
- Real-time election results and statistics
- Election reports and data management
- Audit logging for critical election activities
- Protection against duplicate voting
""",
version="1.0.0",
contact={
    "name": "Prosper Chiedu",
    "email": "prosperchiedu10@gmail.com",
},
docs_url="/docs",
redoc_url="/redoc",
openapi_url="/openapi.json",
)

app.include_router(users_route)