from gen_diff.constants import *
from textwrap import indent


LABEL = {SAVE: ' ',
      REMOVE: '-',
      ADD: '+',
      CHILD: ' ',
      FROM: '-',
      TO: '+'}


def to_string(items):
    diff = ''
    for key, value in items.items():
        if not isinstance(key, tuple):
            diff += '   {}: {}\n'.format(key, value)
        else:
            status, top = key
            diff += '{} {}: {}\n'.format(
                                        LABEL[status],
                                        top,
                                        value
                                        )
    diff = '{}\n{}{}\n'.format('{', diff, '}')
    return diff


def to_format(s):
    diff = s.copy()
    for i in s:
        if type(s[i]) is dict:
            diff[i] = indent(to_format(s[i]), ' ')
    return to_string(diff)
