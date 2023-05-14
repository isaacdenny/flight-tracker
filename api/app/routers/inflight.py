from fastapi import APIRouter
import time

router = APIRouter(prefix="/inflight", tags=["inflight"])

class FlightData():
    uuid: int | 40426
    in_flight = bool | True
    start_time = float | time.time()

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

in_flight_data = FlightData()

@router.get("/")
def get_flight_data():
    return in_flight_data.dict()

@router.post("/{id}/{command}")
async def toggle_flight(id: int, command: str):
    global in_flight_data
    if command is 'start':
        in_flight_data = FlightData()
        return { 'message': 'New flight started, id: ' + in_flight_data.get_id()}
    elif command is 'end':
        if in_flight_data.get_in_flight() and in_flight_data.get_id() is id:
            in_flight_data.set_in_flight(False)
            print(in_flight_data.dict())
