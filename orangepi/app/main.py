import time
import requests

get = False
post = True

server_ip = "192.168.0.20"
server_port = 8000
server_prefix = f"http://{server_ip}:{server_port}/"

velocity_endpoint = "velocity/"
position_endpoint = "position/"

velocity_data = {
    "x": 600.400,
    "y": 43.600,
    "z": 23.670,
}
position_data = {
    "lat":1.600,
    "lon":1.200,
    "alt":2.520
}

def request(endpoint, data=None):
    if data:
      response = requests.post(endpoint, json=data)
    else:
      response = requests.get(endpoint)
    response_json = response.json()
    return response_json

while get:
    v_res = request(server_prefix + velocity_endpoint)
    p_res = request(server_prefix + position_endpoint)

    print("Get Velocity: ", v_res)
    print("Get Position: ", p_res)

    time.sleep(1)

while post:
    v_post_res = request(server_prefix + velocity_endpoint, velocity_data)
    p_post_res = request(server_prefix + position_endpoint, position_data)

    print("Post Velocity: ", v_post_res)
    print("Post Position: ", p_post_res)

    time.sleep(1)