from fastapi import APIRouter, Depends
from app.features.security import verify_token

router = APIRouter(prefix="/velocity", tags=["velocity"])

class Velocity():
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
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
def set_velocity(new_velocity: dict):
    global velocity
    velocity = Velocity(**new_velocity)
    return { "message": "Velocity successfully updated"}