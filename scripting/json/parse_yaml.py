import yaml, sys

path_to_yaml = sys.argv[1]
yaml = yaml.safe_load(open(path_to_yaml).read())
#yaml = yaml.safe_load(open(path_to_yaml, "r"))

for key in yaml:
    value = yaml[key]
    print(f"The key is {key} and the value is {value}")
