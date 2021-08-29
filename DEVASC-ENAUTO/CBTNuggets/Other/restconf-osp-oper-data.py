import requests
import json
from cml_automationlab1 import router1

# GET CAPABILITIES FROM CSR1000V ON CML LAB

# set REST API headers
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

url = f"https://{router1['ip']}:{router1['port']}/restconf/data/Cisco-IOS-XE-ospf-oper:ospf-oper-data/"
# print(url)

response = requests.get(
    url, headers=headers, auth=(router1["user"], router1["password"]), verify=False
)

response_dict = response.json()

print(json.dumps(response_dict, indent=2))

"""if response.status_code == 200:
    for capability in response_dict["capability"]:
        print(capability)
"""
