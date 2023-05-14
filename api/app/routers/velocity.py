from fastapi import APIRouter

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

@router.post("/")
def set_velocity(x: int, y: int, z: int):
    global velocity
    velocity = Velocity(x, y, z)
    return { "message": "Velocity successfully updated"}