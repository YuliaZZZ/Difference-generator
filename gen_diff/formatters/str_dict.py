from gen_diff.generate_diff import get_status, get_key, label
from textwrap import indent


def to_string(items):
    diff = ''
    for key, value in items.items():
        if type(key) is not tuple:
            diff += '   {}: {}\n'.format(key, value)
        else:
            pair = {key: value}
            diff += '{} {}: {}\n'.format(
                                        label[get_status(pair)],
                                        get_key(pair),
                                        value
                                        )
    diff = diff.join(['{\n', '}'])
    return diff


def to_format(s):
    diff = s.copy()
    for i in s:
        if type(s[i]) is dict:
            diff[i] = indent(to_format(s[i]), ' ')
    return to_string(diff)
