added = 'was added with value: '
delete = 'was removed'
change = 'was changed. '


def to_str(status, key, value):
    description = delete
    if status == 'removed':
        value = ''
    elif status == "added" and type(value) is not dict:
        description = added
        value = "'{}'".format(value)
    elif status == "added" and type(value) is dict:
        value = "'complex value'"
        description = added
    elif status == "*":
        description = change
    st = "Property '{}' {}{}.\n".format(key, description, value)
    return st


def to_format(s):
    diff = str_from = ''
    for key in s:
        status, znak, znach = key
        if status == 'changed':
            diff += to_format(changed(znach, s[key]))
        elif status == "from":
            str_from = s[key]
        elif status == "to":
            string = "From '{}' to '{}'".format(str_from, s[key])
            diff += to_str('*', znach, string)
        elif status == 'removed' or status == 'added':
            diff += to_str(status, znach, s[key])
    return diff


def changed(key, value):
    diff = {}
    for i in value:
        status, znak, znach = i
        znach = ".".join([key, znach])
        diff.update({(status, znak, znach): value[i]})
    return diff
