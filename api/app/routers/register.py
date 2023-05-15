from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/register", tags=["register"])


class FieldDevice:
    serial_number: str
    ip_address: str
    device_name: str

    def __init__(self, sn, ip):
        self.serial_number = sn
        self.ip_address = ip

    def get_sn(self):
        return self.serial_number

    def get_ip(self):
        return self.ip_address

    def to_json(self):
        return {
            "serial_number": self.serial_number,
            "ip_address": self.ip_address,
            "device_name": self.device_name,
        }
    
field_devices = []

@router.get('/{sn}')
def get_device_info(sn: str, res: Response):
    for device in field_devices:
        if sn in device:
            return device.to_json()
    res.status_code = status.HTTP_400_BAD_REQUEST
    return { 'error': f'Device with sn: {sn} not found' }

@router.post('/')
def register_device(new_device: dict):
    try:
        device = FieldDevice(**new_device)
        field_devices.add(device)
    except:
        return { 'error': 'Error registering device: ensure sn, ip, and name is correct' }