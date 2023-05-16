from fastapi import APIRouter, Depends
from typing import Annotated
from app.features.security import verify_token

router = APIRouter(prefix="/velocity", tags=["velocity"])

class Velocity():
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def to_json(self):
        return { 'x': self.x, 'y': self.y, 'z': self.z }

velocity = Velocity(0, 0, 0)

@router.get("/")
def get_velocity():
    return velocity.to_json()

@router.post("/", dependencies=[Depends(verify_token)])
def set_velocity(new_velocity: Annotated[Velocity, Depends(Velocity)]):
    global velocity
    velocity = new_velocity
    return { "message": "Velocity successfully updated"}