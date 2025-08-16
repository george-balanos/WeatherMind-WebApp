from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import weather, ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather.router)
app.include_router(ai.router)