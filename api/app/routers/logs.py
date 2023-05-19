from fastapi import APIRouter, Depends, status, Response
from app.database import connection

router = APIRouter(prefix="/logs", tags=["logs"])

keys = ["device_code", "start_time", "total_time", "created_at", "updated_at"]


@router.get("/{device_code}")
def get_device_flight_logs(device_code: str, res: Response):
    with connection.cursor() as db:
        query = f"SELECT * FROM flight_logs WHERE device_code = '{device_code}';"
        db.execute(query)
        result = db.fetchall()
        to_return = []
        for row in result:
            to_return.append({i: j for i, j in zip(keys, row)})
        return result