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
        if f2[k] != v:
            diff[(status['delete'], k)] = v
            diff[(status['added'], k)] = f2[k]
    else:
        diff[(status['delete'], k)] = v
    return diff


def differ(f1, f2):
    diff = {}
    for i in f1:
        if i in f2 and f1[i] != f2[i] and is_child(f1[i], f2[i]):
            diff[i] = differ(f1[i], f2[i])
        else:
            diff.update(to_diff(f2, i, f1[i]))
    for j in f2:
        if j not in f1:
            diff[(status['added'], j)] = f2[j]
    return diff


def formatter(s):
    diff = {}
    for i in s:
        if type(s[i]) is dict:
            for j in s[i]:
                if type(s[i][j]) is dict:
                    s[i][j] = indent(to_string(s[i][j]), '  ')
            else:
                diff[i] = indent(to_string(s[i]), '   ')
        else:
            diff[i] = s[i]
    return to_string(diff)


def engine(file1, file2):
    f1 = parser(file1)
    f2 = parser(file2)
    diff = formatter(differ(f1, f2))
    return diff
