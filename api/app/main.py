from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import register, live, users, logs

app = FastAPI()
app.include_router(register.router)
app.include_router(live.router)
app.include_router(users.router)
app.include_router(logs.router)

origins = [
    "http://localhost:3000",
    "http://localhost:8000/docs"
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