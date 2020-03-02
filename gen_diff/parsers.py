import json
from os.path import split, splitext
import yaml


def parse(file):
    root, name_file = split(file)
    first_name, format = splitext(name_file)
    parsed = json.load(open(file))
    if format == '.json':
        return parsed
    elif format == '.yml':
        parsed = yaml.safe_load(open(file))
        return parsed
