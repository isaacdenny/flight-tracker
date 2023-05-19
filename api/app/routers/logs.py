from fastapi import APIRouter, Response
from app.database import connection

router = APIRouter(prefix="/logs", tags=["logs"])

keys = ["uuid", "device_code", "start_time", "total_time", "created_at", "updated_at"]

pos_keys = ["uuid", "lat", "lon", "alt"]

vel_keys = ["uuid", "x", "y", "z"]



@router.get("/{device_code}")
def get_device_flight_logs(device_code: str, res: Response):
    with connection.cursor() as db:
        query = f"SELECT * FROM flight_logs WHERE device_code = '{device_code}';"
        db.execute(query)
        result = db.fetchall()
        to_return = []
        for row in result:
            to_return.append({i: j for i, j in zip(keys, row)})
        return to_return
    
@router.get("/{flight_id}/positions")
def get_flight_position_logs(flight_id: int):
    with connection.cursor() as db:
        query = f"SELECT * FROM pos_{flight_id}"
        db.execute(query)
        result = db.fetchall()
        to_return = []
        for row in result:
            to_return.append({i: j for i, j in zip(pos_keys, row)})
        return to_return
    
@router.get("/{flight_id}/velocitys")
def get_flight_position_logs(flight_id: int):
    with connection.cursor() as db:
        query = f"SELECT * FROM vel_{flight_id}"
        db.execute(query)
        result = db.fetchall()
        to_return = []
        for row in result:
            to_return.append({i: j for i, j in zip(vel_keys, row)})
        return to_return