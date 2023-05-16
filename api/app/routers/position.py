from fastapi import APIRouter, Depends
from typing import Annotated
from app.features.security import verify_token

router = APIRouter(prefix="/position", tags=["position"])

class Position():
    def __init__(self, lat: float, lon: float, alt: float):
        self.lat = lat
        self.lon = lon
        self.alt = alt

    def to_json(self):
        return { 'lat': self.lat, 'lon': self.lon, 'alt': self.alt}

position = Position(0, 0, 0)

@router.get("/")
def get_position():
    return position.to_json()

@router.post("/", dependencies=[Depends(verify_token)])
def set_position(new_position: Annotated[Position, Depends(Position)]):
    global position
    position = new_position
    return { "message": f"Position successfully updated" }
