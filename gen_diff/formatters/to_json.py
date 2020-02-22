import json


def to_format(s):
    diff = {}
    for i in s:
        status, znak, znach = i
        if status == 'changed':
            s[i] = to_format(s[i])
    for i in s:
        status, znak, znach = i
        if status == 'removed':
            diff[znach] = (status, )
        else:
            diff[znach] = (status, s[i])
    return json.dumps(diff)
