from gen_diff.parsers import parser
from textwrap import indent


status = {'delete': "- ", "added": "+ "}


def to_string(items):
    diff = ''
    for key, value in items.items():
        if type(key) is not tuple:
            diff += '   {}: {}\n'.format(key, value)
        else:
            operator, parameter = key
            diff += '{} {}: {}\n'.format(operator, parameter, value)
    diff = diff.join(['{\n', '}'])
    return diff


def is_child(f1, f2):
    return type(f1) is dict and type(f2) is dict


def to_diff(f2, k, v):
    diff = {}
    if k in f2:
        if f2[k] == v:
            diff[k] = v
        else:
            diff[(status['delete'], k)] = v
            diff[(status['added'], k)] = f2[k]
    else:
        diff[(status['delete'], k)] = v
    return diff


def differ(f1, f2):
    diff = {}
    for key, value in f1.items():
        if key in f2 and value != f2[key] and is_child(value, f2[key]):
            diff[key] = differ(value, f2[key])
        else:
            diff.update(to_diff(f2, key, value))
    for j in f2:
        if j not in f1:
            diff[(status['added'], j)] = f2[j]
    return diff


def formatter(s):
    diff = {}
    for i in s:
        h = s[i]
        if type(h) is not dict:
            diff[i] = h
        else:
            for j in h:
                if is_child(h, h[j]):
                    h[j] = formatter(h[j])
            diff[i] = indent(to_string(h), '   ')
    return to_string(diff)


def engine(file1, file2):
    f1 = parser(file1)
    f2 = parser(file2)
    diff = formatter(differ(f1, f2))
    return diff
