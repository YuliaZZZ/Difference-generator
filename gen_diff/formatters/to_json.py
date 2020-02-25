from gen_diff.generate_diff import get_value, get_status, get_key
import json


def to_format(s):
    s = to_json(s)
    return json.dumps(s)


def to_json(s):
    diff = {}
    for i in s:
        pair = {i: s[i]}
        status = get_status(pair)
        if status == 'removed':
            diff[get_key(pair)] = (status, [])
        if status == 'child':
            diff[get_key(pair)] = to_json(s[i])
        elif status != 'removed' and status != 'child':
            diff[get_key(pair)] = (get_status(pair), s[i])
    return diff
