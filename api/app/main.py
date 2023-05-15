from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import position, velocity, inflight

app = FastAPI()
app.include_router(position.router)
app.include_router(velocity.router)
app.include_router(inflight.router)

origins = [
    "http://192.168.0.20"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get():
    return { "message": "Welcome to the flight tracker API" }