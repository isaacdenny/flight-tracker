class FieldDevice:
    def __init__(
        self, serial_number: str, ip_address: str, device_name: str, device_code: str
    ):
        self.serial_number = serial_number
        self.ip_address = ip_address
        self.device_name = device_name
        self.device_code = device_code

    def get_sn(self):
        return self.serial_number

    def get_ip(self):
        return self.ip_address

    def get_device_name(self):
        return self.device_name

    def get_device_code(self):
        return self.device_code

    def to_json(self):
        return {
            "serial_number": self.serial_number,
            "ip_address": self.ip_address,
            "device_name": self.device_name,
            "device_code": self.device_code,
        }

    def to_values(self):
        return f"'{self.serial_number}', '{self.ip_address}', '{self.device_name}', '{self.device_code}'"