added = 'was added with value: '
delete = 'was removed'
change = 'was changed. '


def to_str(znak, key, value):
    status = delete
    st = ''
    if znak == '- ':
        value = ''
    if znak == "+ " and type(value) is not dict:
        status = added
        value = '"{}"'.format(value)
    if znak == "+ " and type(value) is dict:
        value = "'complex value'"
        status = added
    if znak == "*":
        status = value
        value = ''
    if znak != '  ':
        st = "Property '{}' {}{}.\n".format(key, status, value)
    return st


def format_plain(s):
    diff = str_from = str_to = ''
    for key in s:
        dop, znak, znach = key
        if dop == 'ch':
            diff += changed(znach, s[key])
        if dop == "from":
            str_from = "From '{}'".format(s[key])
        if dop == "to":
            str_to = " to '{}'".format(s[key])
            diff += to_str("*", znach, (change + str_from + str_to))
        if dop == '_':
            diff += to_str(znak, znach, s[key])
    return diff


def changed(key, value):
    diff = {}
    for i in value:
        dop, znak, znach = i
        znach = "{}.{}".format(key, znach)
        diff.update({(dop, znak, znach): value[i]})
    return format_plain(diff)
