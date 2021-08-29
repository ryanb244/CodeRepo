import requests
import json

#####LOGIN####
base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"
user = "devnetuser"
pw = "Cisco123!"

response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user, pw)).json()

token = response["Token"]

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

device_url = "intent/api/v1/network-device?family=Switches and Hubs&type=Cisco Catalyst 9300 Switch"

dev_response = requests.get(
    url=f"{base_url}{device_url}", headers=headers, verify=False
).json()


# print(json.dumps(dev_response, indent=2))

device_Ids = []

for device in dev_response["response"]:
    device_id = device["id"]
    device_Ids.append(device_id)

payload = {"commands": ["show version"], "deviceUuids": device_Ids}

command_endpoint = "intent/api/v1/network-device-poller/cli/read-request"

cli_response = requests.post(
    url=f"{base_url}{command_endpoint}",
    headers=headers,
    data=json.dumps(payload),
    verify=False,
)
