from app.features import crud
from app.features.schema import Position, Velocity


import time


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