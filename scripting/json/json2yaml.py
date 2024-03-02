import json, os, sys, yaml

# Checking if there is a file passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
        print("It worked!")
    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python json2yaml.py <source_json_file.json> <target_yaml_file.yaml>")

# Process the conversion - Use yaml library
# converted_to_yaml = yaml.dump(sys.argv[1], output.yaml)

# Save the conversion in a new file output.yaml

with open(sys.argv[2], 'w') as yaml_file:
    yaml.du
    mp(source_content, yaml_file)