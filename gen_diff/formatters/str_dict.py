from textwrap import indent


def to_string(items):
    diff = ''
    for key, value in items.items():
        if type(key) is not tuple:
            diff += '   {}: {}\n'.format(key, value)
        else:
            _, operator, parameter = key
            diff += '{} {}: {}\n'.format(operator, parameter, value)
    diff = diff.join(['{\n', '}'])
    return diff


def formatter(s):
    diff = s.copy()
    for i in s:
        if type(s[i]) is dict:
            diff[i] = indent(formatter(s[i]), ' ')
    return to_string(diff)
