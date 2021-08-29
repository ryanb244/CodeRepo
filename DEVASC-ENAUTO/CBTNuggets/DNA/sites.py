import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = "devnetuser"
password = "Cisco123!"

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user, password)).json()

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}


"""
#ACCESS SITE API
sites_endpoint = "intent/api/v1/site"

site_response = requests.get(url=f"{base_url}{sites_endpoint}", headers=headers).json()['response']

print(json.dumps(site_response, indent=2))
"""

#ACCESS TOPOLOGY API

topology_endpoint = "intent/api/v1/topology/site-topology"

top_response = requests.get(
    url=f"{base_url}{topology_endpoint}", headers=headers).json()['response']
print(json.dumps(top_response, indent=2))

