import requests
import json
from iosxerouter import xerouter

url = f"https://{xerouter['ip']}:{xerouter['port']}/restconf/data/netconf-state/capabilities"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

response = requests.get(
    url=url,
    headers=headers,
    auth=(xerouter["user"], xerouter["password"]),
    verify=True,
)

response_dict = response.json()["ietf-netconf-monitoring:capabilities"]

# print(response_dict)

if response.status_code == 200:
    for capability in response_dict["capability"]:
        print(capability)
