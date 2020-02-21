added = 'was added with value: '
delete = 'was removed'
change = 'was changed. '


def to_str(znak, key, value):
    status = delete
    st = ''
    if znak == '- ':
        value = ''
    elif znak == "+ " and type(value) is not dict:
        status = added
        value = "'{}'".format(value)
    elif znak == "+ " and type(value) is dict:
        value = "'complex value'"
        status = added
    elif znak == "*":
        status = change
    st = "Property '{}' {}{}.\n".format(key, status, value)
    return st


def format_plain(s):
    diff = str_from = str_to = ''
    for key in s:
        dop, znak, znach = key
        if dop == 'ch':
            diff += format_plain(changed(znach, s[key]))
        elif dop == "from":
            str_from = "From '{}'".format(s[key])
        elif dop == "to":
            str_to = " to '{}'".format(s[key])
            diff += to_str("*", znach, (str_from + str_to))
        elif dop == 'or':
            diff += to_str(znak, znach, s[key])
    return diff


def changed(key, value):
    diff = {}
    for i in value:
        dop, znak, znach = i
        znach = ".".join([key, znach])
        diff.update({(dop, znak, znach): value[i]})
    return diff
