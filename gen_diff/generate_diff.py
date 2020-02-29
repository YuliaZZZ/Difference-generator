from gen_diff.parsers import parser
from gen_diff.constants import *


def is_child(f1, f2):
    return isinstance(f1, dict) and isinstance(f2, dict) and f1 != f2


def differ(f1, f2):
    a = f1.keys()
    b = f2.keys()
    diff = {}
    for i in a&b:
        diff.update(diff_same(i, f1[i], f2[i]))
    for i in a - b:
        diff.update(diff_delete(i, f1[i]))
    for i in b - a:
        diff.update(diff_add(i, f2[i]))
    return diff


def diff_same(i, f1, f2):
    diff = {}
    if f1 == f2:
        diff = make_pair(SAVE, i, f1)
    elif is_child(f1, f2):
        diff = make_pair(CHILD, i, differ(f1, f2))
    elif not is_child(f1, f2):
        diff.update(make_pair(FROM, i, f1))
        diff.update(make_pair(TO, i, f2))
    return diff


def diff_delete(i, f1):
    diff = make_pair(REMOVE, i, f1)
    return diff


def diff_add(i, f2):
    diff = make_pair(ADD, i, f2)
    return diff


def make_pair(status, key, value):
    i = (status, key)
    return {i: value}


def engine(file1, file2, wrapper):
    f1 = parser(file1)
    f2 = parser(file2)
    diff = wrapper(differ(f1, f2))
    return diff
