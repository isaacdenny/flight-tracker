from fastapi import APIRouter, Response, status, Depends
from typing import Annotated
from api.app.features.schema.FieldDevice import FieldDevice
from app.database import connection
from psycopg2.errors import UniqueViolation

router = APIRouter(prefix="/register", tags=["register"])

keys = [
    "serial_number",
    "ip_address",
    "device_name",
    "device_code"
]

@router.get('/{sn}')
async def get_device_info(sn: str, res: Response):
    with connection.cursor() as db:
        query = f"SELECT * FROM devices WHERE serial_number = '{sn}';"
        db.execute(query)
        row = db.fetchone()
        if row is None:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return { 'error': f'Device with sn: {sn} not found' }
        return {i: j for i, j in zip(keys, row[1:])}

@router.post('/')
def register_device(new_device: Annotated[FieldDevice, Depends(FieldDevice)], res: Response):
    with connection.cursor() as db:
        try:
            query = f"SELECT * FROM known_serials WHERE serial_number = '{new_device.get_sn()}'"
            db.execute(query)
            row = db.fetchone()
            if row is None:
                res.status_code = status.HTTP_400_BAD_REQUEST
                return { 'error': 'Error registering device: ensure sn, ip, and name is correct' }
            keys_post = f"{keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}"
            query = f"INSERT INTO devices ({keys_post}) VALUES ({new_device.to_values()}) RETURNING *;"
            db.execute(query)
            row = db.fetchone()
            connection.commit()
            return { 'token': 'fake-super-secret-token', 'device': {i: j for i, j in zip(keys, row[1:])} }
        except UniqueViolation:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return { 'error': 'Error registering device: device already registered' }