import time
import requests

poll_rate = 0.3 # polls per second
in_flight_poll_rate = 5 # polls per second

in_flight = False

server_ip = "192.168.0.10"
server_port = 8000
server_prefix = f"http://{server_ip}:{server_port}/"

velocity_ep = "velocity/"
position_ep = "position/"
in_flight_ep = "inflight/"

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

while True: # or is connected to internet
    res = request(server_prefix + in_flight_ep)
    in_flight = res['in_flight']
    flight_time = res['flight_time']

    if not in_flight:
        print("Flight status: Inactive")
        time.sleep(1 / poll_rate)
    else:
        print("Flight status: Active")
        print("Flight time: ", flight_time)

        v_post_res = request(server_prefix + velocity_ep, velocity_data)
        p_post_res = request(server_prefix + position_ep, position_data)

        print("Updated Velocity: ", v_post_res)
        print("Updated Position: ", p_post_res)
        time.sleep(1 / in_flight_poll_rate)