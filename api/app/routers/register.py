from fastapi import APIRouter, Response, status, Depends
from typing import Annotated
from app.features.classes import FieldDevice

router = APIRouter(prefix="/register", tags=["register"])

field_devices = []

@router.get('/{sn}')
def get_device_info(sn: str, res: Response):
    for device in field_devices:
        if sn == device.get_sn():
            return device.to_json()
    res.status_code = status.HTTP_400_BAD_REQUEST
    return { 'error': f'Device with sn: {sn} not found' }

@router.post('/')
def register_device(new_device: Annotated[FieldDevice, Depends(FieldDevice)], res: Response):
    try:
        if new_device.get_sn() not in known_serials:
            raise Exception
        field_devices.append(new_device)
        return { 'token': 'fake-super-secret-token' }
    except:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return { 'error': 'Error registering device: ensure sn, ip, and name is correct' }