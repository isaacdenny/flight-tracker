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

    def to_json(self):
        return { 'lat': self.lat, 'lon': self.lon, 'alt': self.alt}

position = Position(0, 0, 0)

@router.get("/")
def get_position():
    return position.to_json()

@router.post("/")
def set_position(new_position: dict):
    global position
    position = Position(**new_position)
    return { "message": f"Position successfully updated" }
