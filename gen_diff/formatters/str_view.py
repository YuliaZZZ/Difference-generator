from gen_diff.constants import SAVE, REMOVE, ADD, CHILD, FROM, TO
from textwrap import indent


LABEL = {
      SAVE: ' ',
      REMOVE: '-',
      ADD: '+',
      CHILD: ' ',
      FROM: '-',
      TO: '+'
      }


def diff_sort(i):
    (status, key), value = i
    return key


def to_string(i):
    str_diff = unpack_value = ''
    ((status, key), value) = i
    znak = LABEL[status]
    unpack_key = key
    if status == CHILD or isinstance(value, dict):
        unpack_value = indent(make_format(value, 1), ' ')
    else:
        unpack_value = value
    str_diff += '{} {}: {}\n'.format(znak, unpack_key, unpack_value)
    return str_diff


def make_format(diff, end=0):
    str_diff = ''
    if isinstance(diff, list):
        diff.sort(key=diff_sort)
        for i in diff:
            str_diff += to_string(i)
    else:
        for i in diff:
            str_diff += '   {}: {}\n'.format(i, diff[i])
    str_diff = str_diff.join(['{\n', '}'])
    if end == 0:
        str_diff += '\n'
    return str_diff
