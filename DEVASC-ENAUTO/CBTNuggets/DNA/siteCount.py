import requests
import json


base_url = "https://sandboxdnac.cisco.com/dna/"

auth_endpoint = "system/api/v1/auth/token"

user = "devnetuser"
pw = "Cisco123!"

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user, pw)).json()

token = auth_response["Token"]

site_endpoint = "intent/api/v1/site"

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

site_count = requests.get(
    url=f"{base_url}{site_endpoint}/count", headers=headers
).json()["response"]

print(site_count)
