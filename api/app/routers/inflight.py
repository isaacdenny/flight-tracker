from fastapi import APIRouter, Response, status
import time
import random

router = APIRouter(prefix="/inflight", tags=["inflight"])

class FlightData():
    uuid: int
    in_flight = bool
    start_time = float

    def __init__(self):
        self.uuid = random.randint(0, 9999)
        self.in_flight = True
        self.start_time = time.time()

    def get_id(self):
        return self.uuid

    def get_total_time(self):
        return time.time() - self.start_time
    
    def get_start_time(self):
        return self.start_time
    
    def get_in_flight(self):
        return self.in_flight
    
    def set_in_flight(self, in_flight):
        self.in_flight = in_flight

    def to_json(self):
        return { 'uuid': self.uuid, 'in_flight': self.in_flight, 'start_time': self.start_time, 'total_time': self.get_total_time()}


in_flight_data = None

@router.get("/")
def get_flight_data():
    return in_flight_data.to_json()

@router.post("/{id}/{command}")
async def toggle_flight(id: int, command: str, res: Response):
    global in_flight_data
    if command == 'start':
        in_flight_data = FlightData()
        return { 'message': f'New flight started, id: {in_flight_data.get_id()}'}
    elif command == 'end':
        if in_flight_data is None:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return { 'error': 'No flights currently active' }
        elif in_flight_data.get_id() != id or not in_flight_data.get_in_flight():
            res.status_code = status.HTTP_400_BAD_REQUEST
            return { 'error': 'Flight {id} not currently active' }
        else:
            in_flight_data.set_in_flight(False)
            print(in_flight_data.to_json())
            return { 'message': f'Flight ended, id: {in_flight_data.get_id()}'}
