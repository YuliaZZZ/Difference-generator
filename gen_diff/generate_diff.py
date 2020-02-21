from gen_diff.parsers import parser


status = {'delete': "- ", "added": "+ "}


def is_child(f1, f2):
    return type(f1) is dict and type(f2) is dict and f1 != f2


def to_diff(f2, k, v):
    diff = {}
    if k in f2:
        if f2[k] == v:
            diff[("_", "  ", k)] = v
        else:
            diff[('from', status['delete'], k)] = v
            diff[('to', status['added'], k)] = f2[k]
    else:
        diff[("_", status['delete'], k)] = v
    return diff


def differ(f1, f2):
    diff = {}
    for key, value in f1.items():
        if key in f2 and is_child(value, f2[key]):
            diff[("ch", "  ", key)] = differ(value, f2[key])
        else:
            diff.update(to_diff(f2, key, value))
    for j in f2:
        if j not in f1:
            diff[("_", status['added'], j)] = f2[j]
    return diff


def engine(file1, file2, wrapper):
    f1 = parser(file1)
    f2 = parser(file2)
    diff = wrapper(differ(f1, f2))
    return diff
