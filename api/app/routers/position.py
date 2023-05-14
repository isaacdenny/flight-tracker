from fastapi import APIRouter, Response, status
from pydantic import BaseModel

router = APIRouter(prefix="/position", tags=["position"])

class Position(BaseModel):
    lat: float
    lon: float
    alt: float

position = 0

@router.get("/")
def get_position():
    return position

@router.post("/")
def set_position(new_position: dict, res: Response):
    if (new_position < 0):
        res.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": "Position cannot be lower than 0ft" }
    global position
    position = new_position
    return { "message": f"Position updated to: {position}" }
