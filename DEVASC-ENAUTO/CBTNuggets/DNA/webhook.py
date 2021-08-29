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

events_endpoint = "intent/api/v1/events?tags=ASSURANCE"

events_response = requests.get(
    url=f"{base_url}{events_endpoint}", headers=headers
).json()

print(json.dumps(events_response, indent=2))

events_list = ["NETWORK-NON-FABRIC_WIRED-1-250", "NETWORK-DEVICES-3-207"]

payload = [
    {
        "name": "CBT Nuggets sub",
        "subscriptionEndpoints": [
            {
                "subscriptionDetails": {
                    "connectorType": "REST",
                    "name": "My Azure Python Function App",
                    "description": "ingest payload into CsmosDB",
                    "method": "POST",
                    "url": "https://knoxsfunction.azurewebsites.net/dnaApp",
                }
            }
        ],
        "filter": {"eventIds": events_list},
    }
]

sub_endpoint = "intent/api/v1/event/subscription"

event_sub_response = requests.post(
    url=f"{base_url}{sub_endpoint}", headers=headers, data=json.dumps(payload)
)

print(event_sub_response.status_code)
print(event_sub_response.text)
