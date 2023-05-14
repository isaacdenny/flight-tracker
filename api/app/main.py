from fastapi import FastAPI
from app.routers import position, velocity, inflight

app = FastAPI()
app.include_router(position.router)
app.include_router(velocity.router)
app.include_router(inflight.router)

@app.get("/")
def get():
    return { "message": "Welcome to the flight tracker API" }