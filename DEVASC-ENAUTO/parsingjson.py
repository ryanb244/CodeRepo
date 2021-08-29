import json

# open json file and store as json_data object
with open("json_sample.json") as data:
    json_data = data.read()

# converting data from json file into dictionary
json_dict = json.loads(json_data)

# making change to original data
json_dict["interface"]["description"] = "Backup Link"


# convert python dictionary back to json object and write back to json_sample.json
with open("json_sample.json", "w") as fh:
    json.dump(json_dict, fh, indent=4)
