from gen_diff.parsers import parser


def string(g):
    diff = ''
    for i in g:
        diff += ' {}: {}\n'.format(i, g[i])
    diff = diff.join(['{\n', '}\n'])
    return diff


def difs(f1, f2):
    diff = {}
    for k, v in f1.items():
        if k in f2:
            if v == f2[k]:
                diff["  " + k] = v
            else:
                diff['- ' + k] = v
                diff['+ ' + k] = f2[k]
        else:
            diff['- ' + k] = v
    for k1, v1 in f2.items():
        if k1 not in f1:
            diff['+ ' + k1] = v1
    return diff


def engine(file1, file2):
    f1 = parser(file1)
    f2 = parser(file2)
    diff = difs(f1, f2)
    return string(diff)
