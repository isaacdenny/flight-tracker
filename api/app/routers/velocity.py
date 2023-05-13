from fastapi import APIRouter, Response, status
from pydantic import BaseModel

router = APIRouter(prefix="/velocity", tags=["velocity"])

class Velocity(BaseModel):
    x: int
    y: int
    z: int

velocity = Velocity(0, 0, 0)

@router.get("/")
def get_velocity():
    return velocity

@router.post("/")
def set_velocity(x: int, y: int, z: int, res: Response):
    new_velocity = Velocity(x, y, z)
    global velocity
    velocity = new_velocity
    return { "message": "Velocity successfully updated"}