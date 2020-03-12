from gen_diff.parsers import parsed
from gen_diff.constants import SAVE, ADD, REMOVE, TO, FROM, CHILD


def is_child(f1, f2):
    return isinstance(f1, dict) and isinstance(f2, dict) and f1 != f2


def compare(f1, f2):
    a = f1.keys()
    b = f2.keys()
    diff = list()
    for i in a & b:
        diff.extend(make_diff_same(i, f1[i], f2[i]))
    for i in a - b:
        diff.append(make_diff_delete(i, f1[i]))
    for i in b - a:
        diff.append(make_diff_add(i, f2[i]))
    return diff


def make_diff_same(i, f1, f2):
    diff = {}
    if f1 == f2:
        diff = (make_pair(SAVE, i, f1), )
    elif is_child(f1, f2):
        diff = (make_pair(CHILD, i, compare(f1, f2)), )
    elif not is_child(f1, f2):
        diff = (make_pair(FROM, i, f1), make_pair(TO, i, f2))
    return diff


def make_diff_delete(i, f1):
    return make_pair(REMOVE, i, f1)


def make_diff_add(i, f2):
    return make_pair(ADD, i, f2)


def make_pair(status, key, value):
    return (status, key), value


def generate_diff(file1, file2, vizual):
    f1 = parsed(file1)
    f2 = parsed(file2)
    diff = vizual(compare(f1, f2))
    return diff
