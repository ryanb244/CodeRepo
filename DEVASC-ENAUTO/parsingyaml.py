import yaml

# open yaml file and read data into variable yaml_sample
with open("yaml_sample.yaml") as data:
    yaml_sample = data.read()

# convert yaml data into python dictionary
yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)


# make changes to data
yaml_dict["interface"]["name"] = "GigabitEthernet1"

# write changes back to file
with open("yaml_sample.yaml", "w") as yum:
    yum.write(yaml.dump(yaml_dict, default_flow_style=False))
