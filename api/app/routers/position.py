from fastapi import APIRouter

router = APIRouter(prefix="/position", tags=["position"])

class Position():
    lat: float
    lon: float
    alt: float

    def __init__(self, lat, lon, alt):
        self.lat = lat
        self.lon = lon
        self.alt = alt

position = Position(0, 0, 0)

@router.get("/")
def get_position():
    return position.dict()

@router.post("/")
def set_position(lat: int, lon: int, alt: int):
    global position
    position = Position(lat, lon, alt)
    return { "message": f"Position updated to: {position}" }
