import random


class User:
    def __init__(self, username: str, email: str, password: str, device_code: str):
        self.username = username
        self.email = email
        self.password = password
        self.device_code = device_code

    def get_email(self):
        return self.email

    def get_device_code(self):
        return self.device_code

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "device_code": self.device_code,
        }

    def to_values(self):
        return f"'{self.username}', '{self.email}', '{self.password}', '{self.device_code}'"