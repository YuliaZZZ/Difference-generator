import json


def st(a, b):
    return ' {}: {}\n'.format(a, b)


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    new = f1.copy()
    new.update(f2)
    diff = '{\n'
    for i in new:
        if i not in f2:
            diff += '-' + st(i, new.get(i))
        if f1.get(i) == f2.get(i):
            diff += ' ' + st(i, new.get(i))
        if i in f1 and f1.get(i) != new.get(i):
            diff += '-' + st(i, f1.get(i)) + '+' + st(i, new.get(i))
        if i not in f1:
            diff += '+' + st(i, new.get(i))
    diff = diff + '}'
    return diff
