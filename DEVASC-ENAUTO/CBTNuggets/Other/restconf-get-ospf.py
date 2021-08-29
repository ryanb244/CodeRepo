import requests
import json
from cml_automationlab1 import router1


# set REST API headers
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

url = f"https://{router1['ip']}:{router1['port']}/restconf/data/Cisco-IOS-XE-ospf-oper:ospf-oper-data/ospf-state/ospf-instance=address-family-ipv4, 168430081/ospf-area=0/ospf-interface=GigabitEthernet2/ospf-neighbor=10.10.10.2/state"
# print(url)

response = requests.get(
    url, headers=headers, auth=(router1["user"], router1["password"]), verify=False
).json()

print(json.dumps(response, indent=2))
