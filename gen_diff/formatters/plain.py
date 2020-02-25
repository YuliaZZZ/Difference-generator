from gen_diff.generate_diff import get_value, get_status, get_key, make_pair


def to_str(pair):
    end = ''
    if get_status(pair) == 'removed':
        end = '.\n'
    if get_status(pair) == 'changed':
        end = ". From '{}' to ".format(get_value(pair))
    if get_status(pair) == 'added':
        end = " with value: '{}'.\n".format(get_value(pair))
    st = "Property '{}' was {}{}".format(get_key(pair), get_status(pair), end)
    return st


def to_format(s):
    diff = ''
    for key in s:
        pair = {key: s[key]}
        if get_status(pair) == 'child':
            diff += to_format(stepper(pair))
        else:
            diff += selection(pair)
    return diff


def stepper(pair):
    s = get_value(pair)
    diff = {}
    for i in s:
        pairs = {i: s[i]}
        new_i = ".".join([get_key(pair), get_key(pairs)])
        diff.update(make_pair(get_status(pairs), new_i, s[i]))
    return diff


def selection(pair):
    status = get_status(pair)
    if status == 'added' and type(get_value(pair)) is dict:
        pair = make_pair(status, get_key(pair), "complex value")
    if status == 'to':
        string = "'{}'.\n".format(get_value(pair))
        return string
    elif status == 'no change':
        return ''
    return to_str(pair)
