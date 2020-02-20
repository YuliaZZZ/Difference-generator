added = 'was added with value: '
delete = 'was removed'
change = 'was changed. '


def to_str(key, status):
    st = 'Property "{}" {}.\n'.format(key, status)
    return st


def str_add(key, value, status):
    znach = "'complex value'"
    if type(value) is not dict:
        znach = "'{}'".format(value)
    status += znach
    st = to_str(key, status)
    return st


def format_plain(s):
    diff = ''
    for key in s:
        dop, znak, znach = key
        if dop == 'ch':
            diff += changed(znach, s[key], change)
        else:
            if znak == '- ':
                diff += to_str(znach, delete)
            elif znak == "+ ":
                diff += str_add(znach, s[key], added)
    return diff


def changed(key, value, status):
    f = j = diff = ''
    for i in value:
        dop, znak, znach = i
        znach = "{}.{}".format(key, znach)
        if dop == "cna":
            if znak == "- ":
                j = "From '{}'".format(value[i])
            elif znak == "+ ":
                f = " to '{}'".format(value[i])
            diff = to_str(znach, (change + j + f))
        else:
            diff += format_plain({(dop, znak, znach): value[i]})
    return diff
