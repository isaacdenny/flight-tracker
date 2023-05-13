from fastapi import FastAPI
from app.routers import altitude

app = FastAPI()
app.include_router(altitude.router)

@app.get("/")
def get():
    return { "message": "Welcome to the flight tracker API" }
