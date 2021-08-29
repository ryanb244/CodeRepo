import xmltodict

# open xml file and store data in python object xml_example
with open("xml_sample.xml") as data:
    xml_example = data.read()

# convert xml data to python dictionary
xml_dict = xmltodict.parse(xml_example)

print(xml_dict)

# change value for IP address
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

print(xmltodict.unparse(xml_dict, pretty=True))

# write changes back to original file
with open("xml_sample.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))
