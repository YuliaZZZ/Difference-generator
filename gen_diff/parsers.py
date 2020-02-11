import json
from os.path import split, splitext
import yaml


def parser(file):
    root, name_file = split(file)
    first_name, format = splitext(name_file)
    parse = json.load(open(file))
    if format == '.json':
        return parse
    elif format == '.yml':
        parse = yaml.safe_load(open(file))
        return parse
