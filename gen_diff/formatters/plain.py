added = 'was added with value: '
delete = 'was removed'
change = 'was changed'


def to_str(key, description, value):
    if description == change:
        st = "Property '{}' {}. From '{}' to '".format(key, description, value)
    else:
        st = "Property '{}' {}{}.\n".format(key, description, value)
    return st


def to_format(s):
    diff = ''
    for key in s:
        status, _, znach = key
        if status == 'changed':
            diff += to_format(changed(znach, s[key]))
        else:
            diff += selection(key, s[key])
    return diff


def changed(key, value):
    diff = {}
    for i in value:
        status, znak, znach = i
        znach = ".".join([key, znach])
        diff.update({(status, znak, znach): value[i]})
    return diff


def selection(key, value):
    status, _, znach = key
    description = delete
    if status == 'removed':
        value = ''
    if status == "added" and type(value) is not dict:
        description = added
        value = "'{}'".format(value)
    if status == "added" and type(value) is dict:
        value = "'complex value'"
        description = added
    if status == "from":
        description = change
    if status == "to":
        string = "{}'.\n".format(value)
        return string
    if status == "no change":
        return ''
    return to_str(znach, description, value)
