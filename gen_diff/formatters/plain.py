added = 'was added with value: '
delete = 'was removed'
change = 'was changed. '


def to_str(znak, key, value):
    status = delete
    if znak == '- ':
        value = ''
    if znak == "+ " and type(value) is not dict:
        status = added
        value = "'{}'".format(value)
    if znak == "+ " and type(value) is dict:
        value = "'complex value'"
        status = added
    if znak == "c":
        status = value
        value = ''
    st = "Property '{}' {}{}.\n".format(key, status, value)
    return st


def format_plain(s):
    diff = ''
    for key in s:
        dop, znak, znach = key
        if dop == 'ch':
            diff += changed(znach, s[key])
        elif znak == '- ' or znak == "+ ":
            diff += to_str(znak, znach, s[key])
    return diff


def changed(key, value):
    f = j = diff = ''
    for i in value:
        dop, znak, znach = i
        znach = "{}.{}".format(key, znach)
        if dop == "cna" and znak == "- ":
            j = 'From "{}"'.format(value[i])
        if dop == "cna" and znak == "+ ":
            f = ' to "{}"'.format(value[i])
            diff = to_str("c", znach, (change + j + f))
        else:
            diff += format_plain({(dop, znak, znach): value[i]})
    return diff
