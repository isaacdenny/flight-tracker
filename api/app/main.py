from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import register, live, users

app = FastAPI()
app.include_router(register.router)
app.include_router(live.router)
app.include_router(users.router)

origins = [
    "http://localhost:3000",
    "http://localhost:8000/docs"
]

field_ips = [device.get_ip() for device in register.field_devices]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins + field_ips,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get():
    return { "message": "Welcome to the flight tracker API" }