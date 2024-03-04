import json, os, sys, yaml

# Checking if there is a file passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
        print("It worked!")
    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python yaml2json.py <source_yaml_file.yaml> <target_json_file.json>")

with open(sys.argv[2], 'w') as json_file:
    json.dump(source_content, json_file, indent=4)