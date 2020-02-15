from gen_diff.parsers import parser


def diff_to_string(f):
    diff = ''
    for i in f:
        diff += ' {}: {}\n'.format(i, f[i])
    diff = diff.join(['{\n', '}\n'])
    return diff


def difs(f, k, v):
    diff = {}
    if k in f:
        if v == f[k]:
            diff["  " + k] = v
        else:
            diff['- ' + k] = v
            diff['+ ' + k] = f[k]
    else:
        diff['- ' + k] = v
    return diff


def differ(f1, f2):
    diff = {}
    for k, v in f1.items():
        diff.update(difs(f2, k, v))
    for k1, v1 in f2.items():
        if k1 not in f1:
            diff.update({'+ ' + k1: v1})
    return diff


def engine(file1, file2):
    f1 = parser(file1)
    f2 = parser(file2)
    return diff_to_string(differ(f1, f2))
