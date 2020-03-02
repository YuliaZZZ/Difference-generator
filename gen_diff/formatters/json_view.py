import json
from gen_diff.formatters.str_view import diff_sort


def make_format(diff):
    diff.sort(key=diff_sort)
    return json.dumps(diff) + '\n'
