import json


STATUS = {'deleted': '- ', 'added': '+ '}


def string(a, b, z='  '):
    return '{} {}: {}\n'.format(z, a, b)


def difs(d, k, v):
    if k in d:
        if d[k] == v:
            return string(k, v)
        else:
            st = string(k, v, STATUS['deleted'])
            st = st + string(k, d[k], STATUS['added'])
            return st
    else:
        return string(k, v, STATUS['deleted'])


def engine(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    diff = ''
    for k, v in f1.items():
        diff += difs(f2, k, v)
    for k1, v1 in f2.items():
        if k1 not in f1:
            diff += string(k1, v1, STATUS['added'])
    diff = diff.join(['{\n', '}\n'])
    return diff
