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

def request(prefix, endpoint, data):
    response = requests.post(prefix + endpoint, json=data)
    response_json = response.json()
    return response_json

while get:
    # The API endpoint
    url = f"https://{server_ip}:{server_port}"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)

while post:
    v_post_res = request(server_prefix, velocity_endpoint, velocity_data)
    p_post_res = request(server_prefix, position_endpoint, position_data)
    
    print("Velocity response: ", v_post_res)
    print("Position response: ", p_post_res)