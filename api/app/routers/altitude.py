from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/altitude", tags=["altitude"])

altitude = 0

@router.get("/")
def get_altitude():
    return altitude

@router.post("/")
def set_altitude(new_altitude: int, res: Response):
    if (new_altitude < 0):
        res.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": "Altitude cannot be lower than 0ft" }
    global altitude;
    altitude = new_altitude
    return { "message": f"Altitude updated to: {altitude}" }
