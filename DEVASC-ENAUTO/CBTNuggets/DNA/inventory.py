import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = "devnetuser"
password = "Cisco123!"

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password)
).json()

token = auth_response["Token"]

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# GET DEVICE INVENTORY
device_endpoint = "intent/api/v1/network-device"

dev_response = requests.get(url=f"{base_url}{device_endpoint}", headers=headers).json()[
    "response"
]

print(json.dumps(dev_response, indent=2))
