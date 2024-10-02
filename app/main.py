from fastapi import FastAPI
from .routers import users
from .database import engine
from .models import Base

# Initialize FastAPI
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include the user routes
app.include_router(users.router)
