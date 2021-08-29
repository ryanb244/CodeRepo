
import requests
import json
from pprint import pprint
import shutil
import os

################## LOGIN ################
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(url, auth=(user, pw)).json()
# print(response)
token = response['Token']

############### GET CLIENT HEALTH STATUS ##################

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

querystring = {"timestamp": ""}

headers = {
    'x-auth-token': token,
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "393a9fdd-f109-4fd3-821b-0ae2a03da256,3d2299b4-7515-4f80-9964-b33c2ae9c2ab",
    'Host': "sandboxdnac2.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.get(url, headers=headers, params=querystring).json()

with open("Clienthealthdata.txt", "w+") as file:
    file.write(str(response))


shutil.move('C:\\Users\\Ryan\\Google Drive\\CodeRepo\\Clienthealthdata.txt',
            'C:\\Users\\Ryan\\Google Drive\\CodeRepo\\DEVASC-ENAUTO\\CBTNuggets')

print(f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f" {score_value['scoreCategory']['value']}: {score_value['clientCount']}"
            )
