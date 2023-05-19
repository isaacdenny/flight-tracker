from fastapi import APIRouter, Depends, status, Response
from app.features.security import verify_token
from typing import Annotated
from app.features.schema.Velocity import Velocity
from app.features.schema.Position import Position
from app.features.schema.Flight import Flight

router = APIRouter(prefix="/live", tags=["live"])


flights = []


@router.get("/{device_code}")
def get_flight_data(device_code: str, res: Response):
    for flight in flights:
        if flight.get_device_code() == device_code:
            return flight.to_json()
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No flight matches device_code: {device_code}"}


@router.post("/{device_code}")
def start_flight(device_code: str, res: Response):
    # check to see if device is registered
    for flight in flights:
        if flight.get_device_code() == device_code:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {
                "error": f"User with device: {device_code} already in flight. End active flight first"
            }
    new_flight = Flight(device_code)
    flights.append(new_flight)
    return {"message": "Flight successfully started"}


@router.post("/{device_code}/end")
async def end_flight(device_code: str, res: Response):
    for flight in flights:
        if flight.get_device_code() == device_code:
            flights.remove(flight)
            flight.end()
            return {"message": f"Flight successfully ended"}
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"Flight with device_code: {device_code} not currently active"}


@router.post("/{device_code}/velocity", dependencies=[Depends(verify_token)])
def set_velocity(device_code: str, new_velocity: Annotated[Velocity, Depends(Velocity)], res: Response):
    for flight in flights:
        if flight.get_device_code() == device_code:
            flight.set_velocity(new_velocity)
            return {"message": "Velocity successfully updated"}
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No flight for device code: {device_code}"}


@router.post("/{device_code}/position", dependencies=[Depends(verify_token)])
def set_position(device_code: str, new_position: Annotated[Position, Depends(Position)], res: Response):
    for flight in flights:
        if flight.get_device_code() == device_code:
            flight.set_position(new_position)
            return {"message": "Position successfully updated"}
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No flight for device code: {device_code}"}
