import json


def to_format(s):
    s = change_diff(s)
    diff = {}
    for i in s:
        status, _, znach = i
        if status == 'changed':
            diff[znach] = (status, to_format(s[i]))
        else:
            diff[znach] = (status, s[i])
    return json.dumps(diff)


def change_diff(s):
    for i in s:
        status, znak, znach = i
        if status == 'removed':
            s[i] = []
        if status == 'changed':
            s[i] = change_diff(s[i])
    return s
