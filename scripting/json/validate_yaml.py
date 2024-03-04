import yaml, sys, os, json
from jsonschema import validate

# schema = '''
# type: object
# '''
#
# path_to_yaml = "output.yaml"
#
# yaml_instance = yaml.safe_load(open(path_to_yaml).read())
#
# validate(yaml_instance, yaml.safe_load(schema))
#
#
# path_to_json = "example.json"
# test_instance = json.loads(open(path_to_json).read())
#
# validate(test_instance, yaml.safe_load(schema))

if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
        print("YAML is valid!")
    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python validate_yaml.py <yaml_file.yaml>")
