import json
import os.path
import yaml


def parsed(file):
    root, name_file = os.path.split(file)
    first_name, format = os.path.splitext(name_file)
    if format == '.json':
        parsed = json.load(open(file))
    elif format == '.yml':
        parsed = yaml.safe_load(open(file))
    # else:
    #    with open(file, 'r') as input_file:
    #        parsed = input_file.read()
    return parsed
