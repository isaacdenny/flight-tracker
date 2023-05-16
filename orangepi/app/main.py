import requests
import os, sys, time
from dotenv import load_dotenv

load_dotenv()

poll_rate = 0.3  # polls per second
in_flight_poll_rate = 5  # polls per second

serial_number = os.getenv("SERIAL_NUMBER")
public_ip = os.getenv("PUBLIC_IP")
device_name = os.getenv("DEVICE_NAME")

server_host = os.getenv("SERVER_HOST")
server_port = os.getenv("SERVER_PORT")
server_url = f"http://{server_host}:{server_port}/"

device_info = {
    "serial_number": serial_number,
    "ip_address": public_ip,
    "device_name": device_name,
}

velocity_ep = "velocity/"
position_ep = "position/"
in_flight_ep = "inflight/"
register_ep = "register/"

is_registered = False
is_online = True
in_flight = False

velocity_data = {
    "x": 600.400,
    "y": 43.600,
    "z": 23.670,
}
position_data = {"lat": 1.600, "lon": 1.200, "alt": 2.520}


def check_online():
    try:
        requests.get("https://dns.google.com/")
        print("Status: Tether Online")
        return True
    except Exception as e:
        print(e)
        return False


# REGISTER DEVICE
if not check_online():
    sys.exit()

try:
    register_res = requests.post(
        server_url + register_ep, json=device_info
    ).json()
    if 'token' not in register_res:
        raise Exception('No token')
    token = register_res['token']
    is_registered = True
except Exception as e:
    print(f"Error registering {serial_number}: {e}")
    sys.exit()


# POLL API
while True:
    try:
        res = requests.get(server_url + in_flight_ep, headers={"x_token": token}).json()
        in_flight = res["in_flight"]

        if not in_flight:
            print("Flight status: Inactive")
            time.sleep(1 / poll_rate)
        else:
            total_flight_time = res["total_time"]
            print("Flight status: Active")
            print("Flight time: ", total_flight_time)
            v_post_res = requests.post(
                server_url + velocity_ep, json=velocity_data, headers={"x_token": token}
            ).json()
            p_post_res = requests.post(
                server_url + position_ep, json=position_data, headers={"x_token": token}
            ).json()
            print("Updated Velocity: ", v_post_res)
            print("Updated Position: ", p_post_res)
            time.sleep(1 / in_flight_poll_rate)
    except Exception as e:
        print(f"Error requesting {server_host}: {e}")
        time.sleep(2)
