from fastapi import APIRouter, Depends, status, Response
from app.features.security import verify_token
from typing import Annotated
from app.features.classes import Position, Flight, Velocity

router = APIRouter(prefix="/live", tags=["live"])


flights = []


@router.get("/{uuid}")
def get_flight_data(uuid: int, res: Response):
    for flight in flights:
        if flight.get_uuid() == uuid:
            return flight.to_json()
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No flight matches id: {uuid}"}


@router.post("/{device_code}")
def start_flight(device_code: int, res: Response):
    for flight in flights:
        if flight.get_device_code() == device_code:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {
                "error": f"User with device: {device_code} already in flight id: {flight.get_uuid()}. End active flight first"
            }
    new_flight = Flight(device_code)
    flights.append(new_flight)
    return {"uuid": new_flight.get_uuid()}


@router.post("/{uuid}/end")
async def end_flight(uuid: int, res: Response):
    for flight in flights:
        if flight.get_uuid() == uuid and flight.get_is_active():
            flight.set_is_active(False)
            return {"message": f"Flight successfully ended"}
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"Flight with id: {uuid} not currently active"}


@router.post("/{uuid}/velocity", dependencies=[Depends(verify_token)])
def set_velocity(uuid: int, new_velocity: Annotated[Velocity, Depends(Velocity)], res: Response):
    for flight in flights:
        if flight.get_uuid() == uuid:
            flight.set_velocity(new_velocity)
            return {"message": "Velocity successfully updated"}
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No flight matching id: {uuid}"}


@router.post("/{uuid}/position", dependencies=[Depends(verify_token)])
def set_position(uuid: int, new_position: Annotated[Position, Depends(Position)], res: Response):
    for flight in flights:
        if flight.get_uuid() == uuid:
            flight.set_position(new_position)
            return {"message": "Position successfully updated"}
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"No flight matching id: {uuid}"}
