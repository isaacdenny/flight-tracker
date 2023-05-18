import random, time

class Position():
    def __init__(self, lat: float, lon: float, alt: float):
        self.lat = lat
        self.lon = lon
        self.alt = alt

    def to_json(self):
        return { 'lat': self.lat, 'lon': self.lon, 'alt': self.alt}
    
class Velocity():
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def to_json(self):
        return { 'x': self.x, 'y': self.y, 'z': self.z }

class Flight:
    def __init__(self, user_id: str):
        self.uuid = random.randint(0, 9999)
        self.user_id = user_id
        self.is_active = True
        self.start_time = time.time()
        self.position = Position(0, 0, 0)
        self.velocity = Velocity(0, 0, 0)

    def get_uuid(self):
        return self.uuid

    def get_user_id(self):
        return self.user_id

    def get_total_time(self):
        return time.time() - self.start_time

    def get_start_time(self):
        return self.start_time

    def get_is_active(self):
        return self.is_active

    def set_is_active(self, is_active):
        self.is_active = is_active

    def get_velocity(self):
        return self.velocity.to_json()
    
    def get_position(self):
        return self.position.to_json()

    def set_velocity(self, velocity: Velocity):
        self.velocity = velocity
    
    def set_position(self, position: Position):
        self.position = position

    def to_json(self):
        return {
            "uuid": self.uuid,
            "user_id": self.user_id,
            "is_active": self.is_active,
            "start_time": self.start_time,
            "total_time": self.get_total_time(),
            "position": self.position.to_json(),
            "velocity": self.velocity.to_json()
        }