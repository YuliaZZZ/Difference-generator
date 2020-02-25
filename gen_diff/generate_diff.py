from gen_diff.parsers import parser


label = {
      'removed': '-',
      'added': '+',
      'child': ' ',
      'changed': '-',
      'to': '+',
      'no change': ' '}


def is_child(f1, f2):
    return type(f1) is dict and type(f2) is dict and f1 != f2


def differ(f1, f2):
    a = set(f1)
    b = set(f2)
    same = list(a & b)
    same.sort()
    change = list(a ^ b)
    change.sort()
    diff = {}
    diff.update(diff_same(same, f1, f2))
    diff.update(diff_change(change, f1, f2))
    return diff


def diff_same(itog_set, f1, f2):
    diff = {}
    for i in itog_set:
        if f1[i] == f2[i]:
            diff.update(make_pair('no change', i, f1[i]))
        elif f1[i] != f2[i] and is_child(f1[i], f2[i]):
            diff.update(make_pair('child', i, differ(f1[i], f2[i])))
        elif f1[i] != f2[i] and not is_child(f1[i], f2[i]):
            diff.update(make_pair('changed', i, f1[i]))
            diff.update(make_pair('to', i, f2[i]))
    return diff


def diff_change(itog_set, f1, f2):
    diff = {}
    for i in itog_set:
        if i in set(f1) - set(f2):
            diff.update(make_pair('removed', i, f1[i]))
        if i in set(f2) - set(f1):
            diff.update(make_pair('added', i, f2[i]))
    return diff


def make_pair(status, key, value):
    i = (status, key)
    return {i: value}


def get_key(pair):
    ((status, key), ) = pair.keys()
    return key


def get_value(pair):
    ((value), ) = pair.values()
    return value


def get_status(pair):
    ((status, key), ) = pair.keys()
    return status


def engine(file1, file2, wrapper):
    f1 = parser(file1)
    f2 = parser(file2)
    diff = wrapper(differ(f1, f2))
    return diff
