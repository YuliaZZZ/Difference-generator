import json
from os.path import split, splitext


def parser(file):
    root, name = split(file)
    format = splitext(name)
    first_name, last_name = format
    parse = json.load
    if last_name == '.json':
        return parse
    elif last_name == '.yml':
        parse = yaml.safeLoad
        return parse
