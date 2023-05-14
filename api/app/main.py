from fastapi import FastAPI
from app.routers import position, velocity

app = FastAPI()
app.include_router(position.router)
app.include_router(velocity.router)

@app.get("/")
def get():
    return { "message": "Welcome to the flight tracker API" }