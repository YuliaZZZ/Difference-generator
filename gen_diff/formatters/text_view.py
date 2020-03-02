from gen_diff.engine import make_pair
from gen_diff.formatters.str_view import diff_sort
from gen_diff.constants import SAVE, REMOVE, ADD, CHILD, FROM, TO


def to_string(i):
    appendix = ''
    (status, key), value = i
    if status == REMOVE:
        appendix = '.\n'
    if status == FROM:
        appendix = ". From '{}' to ".format(value)
    if status == ADD:
        appendix = " with value: '{}'.\n".format(value)
    st = "Property '{}' was {}{}".format(key, status, appendix)
    return st


def selecte(i):
    (status, key), value = i
    if status == ADD and type(value) is dict:
        i = make_pair(status, key, 'complex value')
    if status == TO:
        string = "'{}'.\n".format(value)
        return string
    if status == SAVE:
        return ''
    return to_string(i)


def make_format(diff):
    str_diff = ''
    diff.sort(key=diff_sort)
    for i in diff:
        (status, key), value = i
        if status == CHILD:
            str_diff += make_format(deepen(key, value))
        else:
            str_diff += selecte(i)
    return str_diff


def deepen(key, value):
    new_diff = list()
    for i in value:
        (status_v, key_v), value_v = i
        new_key = ".".join([key, key_v])
        new_diff.append(make_pair(status_v, new_key, value_v))
    return new_diff
