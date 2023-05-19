import random, time
from app.database import connection
from app.features import crud


class User:
    def __init__(self, username: str, email: str, password: str, device_code: str):
        self.uuid = random.randint(0, 9999)
        self.username = username
        self.email = email
        self.password = password
        self.device_code = device_code

    def get_uuid(self):
        return self.uuid

    def get_email(self):
        return self.email

    def get_device_code(self):
        return self.device_code

    def to_json(self):
        return {
            "uuid": self.uuid,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "device_code": self.device_code,
        }

    def to_values(self):
        return f"'{self.username}', '{self.email}', '{self.password}', '{self.device_code}'"


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


class Position:
    def __init__(self, lat: float, lon: float, alt: float):
        self.lat = lat
        self.lon = lon
        self.alt = alt
    
    def get_lat(self):
        return self.lat
    
    def get_lon(self):
        return self.lon
    
    def get_alt(self):
        return self.alt

    def to_json(self):
        return {"lat": self.lat, "lon": self.lon, "alt": self.alt}


class Velocity:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z

    def to_json(self):
        return {"x": self.x, "y": self.y, "z": self.z}


class Flight:
    def __init__(self, device_code: str):
        self.device_code = device_code
        self.start_time = time.time()
        self.positions = [Position(0, 0, 0)]
        self.velocitys = [Velocity(0, 0, 0)]

    def get_device_code(self):
        return self.device_code

    def get_total_time(self):
        return time.time() - self.start_time

    def get_start_time(self):
        return self.start_time

    def get_velocity(self):
        return self.velocitys.pop().to_json()

    def get_position(self):
        return self.positions.pop().to_json()

    def set_velocity(self, new_velocity: Velocity):
        self.velocitys.append(new_velocity)

    def set_position(self, new_position: Position):
        self.positions.append(new_position)

    def end(self):
        crud.log_flight(self, self.positions, self.velocitys)

    def to_json(self):
        return {
            "device_code": self.device_code,
            "start_time": self.start_time,
            "total_time": self.get_total_time(),
            "position": self.get_position(),
            "velocity": self.get_velocity(),
        }

    def to_values(self):
        return f"'{self.device_code}', {self.start_time}, {self.get_total_time()}"
