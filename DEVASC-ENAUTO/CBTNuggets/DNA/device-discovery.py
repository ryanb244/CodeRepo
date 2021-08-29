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


# CLI CREDENTIALS
cred_cli_endpoint = "intent/api/v1/global-credential?credentialSubType=CLI"

cli_response = requests.get(
    url=f"{base_url}{cred_cli_endpoint}", headers=headers
).json()["response"][0]

cli_cred = cli_response["id"]

# SNMP CREDENTIALS
cred_snmp_endpoint = (
    "intent/api/v1/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY"
)

snmp_response = requests.get(
    url=f"{base_url}{cred_snmp_endpoint}", headers=headers
).json()["response"][0]

snmp_cred = snmp_response["id"]

payload = {
    "name": "CBT Nuggets Discovery",
    "discoveryType": "range",
    "ipAddressList": "10.10.20.30-10.10.20.254",
    "timeout": 1,
    "protocolOrder": "ssh,telnet",
    "preferredMgmtIpMethod": "None",
    "globalCredentialList": [cli_cred, snmp_cred],
}

discovery_endpoint = "intent/api/v1/discovery"

disc_response = requests.post(
    url=f"{base_url}{discovery_endpoint}", headers=headers, data=json.dumps(payload)
)

print(disc_response)
print(disc_response.text)
