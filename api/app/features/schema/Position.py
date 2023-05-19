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