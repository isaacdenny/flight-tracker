import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

poll_rate = 0.3 # polls per second
in_flight_poll_rate = 5 # polls per second

in_flight = False

server_host = os.getenv('SERVER_HOST')
server_port = os.getenv('SERVER_PORT')
server_url = f"http://{server_host}:{server_port}/"

is_online = True

velocity_ep = "velocity/"
position_ep = "position/"
in_flight_ep = "inflight/"

velocity_data = {
    'x': 600.400,
    'y': 43.600,
    'z': 23.670,
}
position_data = {
    'lat': 1.600,
    'lon': 1.200,
    'alt': 2.520
}

def request(endpoint, data=None):
    if data:
        response = requests.post(endpoint, json=data)
    else:
        response = requests.get(endpoint)
    response_json = response.json()
    return response_json

while is_online: # or is connected to internet
    try:
        res = request(server_url + in_flight_ep)
        in_flight = res['in_flight']
        
        if not in_flight:
            print("Flight status: Inactive")
            time.sleep(1 / poll_rate)
        else:
            total_flight_time = res['total_time']
            print("Flight status: Active")
            print("Flight time: ", total_flight_time)
            v_post_res = request(server_url + velocity_ep, velocity_data)
            p_post_res = request(server_url + position_ep, position_data)
            print("Updated Velocity: ", v_post_res)
            print("Updated Position: ", p_post_res)
            time.sleep(1 / in_flight_poll_rate)
    except Exception as e:
        print(f"Error requesting {server_host}: {e}")
        time.sleep(2)