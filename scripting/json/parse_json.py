import os, json

path_to_json = "example.json"
json = json.loads(open(path_to_json).read())
#json = json.load(open(path_to_json, "r"))

for key in json:
    value = json[key]
    print(f"The key is {key} and the value is {value}")