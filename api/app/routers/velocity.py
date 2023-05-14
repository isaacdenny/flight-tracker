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

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z

velocity = Velocity(0, 0, 0)

@router.get("/")
def get_velocity():
    return velocity

@router.post("/")
def set_velocity(x: int, y: int, z: int):
    global velocity
    new_velocity = Velocity(x, y, z)
    velocity = new_velocity
    return { "message": "Velocity successfully updated"}