import sys, os, subprocess, json

# os
# os.mkdir("test-dir")

# sys
# if len(sys.argv) > 1:
#     print("You gave me an argument!")

# subprocess
subprocess.run(["python","hello_world.py"])

# json
dict = {
    "name": "Ramon",
    "age": "23",
    "city": "Manchester"
}

json_dict = json.dumps(dict)
print(dict)
print(type(dict))
print()
print(json_dict)
print(type(json_dict))