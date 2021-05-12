import json

#load json from file
jsonobj = json.load(open('sample.json'))

print(jsonobj['people'])

#load json from string
jsonstr = """{
    "people": [
        {
            "Id": "1",
            "FirstName": "Benjamin",
            "LastName": "Finkel",
            "Email": "ben.finkel@cbtnuggets"
        },
        {
            "Id": "2",
            "FirstName": "Jane",
            "LastName": "Doe",
            "Email": "jane.doe@cbtnuggets.com"
        },
        {
            "Id": "3",
            "FirstName": "Pat",
            "LastName": "Smith",
            "Email": "pat.smith@cbtnuggets"
        }
    ]
}"""

jsonobj = json.loads(jsonstr)

print(jsonobj)