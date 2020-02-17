# -*- coding:utf-8 -*-
import pytest
import yaml
from gen_diff import generate_diff, parsers


file = open('./tests/fixtures/result.txt', 'r')
answer = file.read()


file1 = open('./tests/fixtures/recursion_result.txt', 'r')
answer2 = file1.read()


def test_answer():
    assert answer == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json') + '\n'
    assert yaml.safe_load(open('./tests/fixtures/before.yml')) == parsers.parser('./tests/fixtures/before.yml')
    assert type(generate_diff.engine('./tests/fixtures/before.yml', './tests/fixtures/after.yml')) is str
    assert answer2 == generate_diff.engine('./tests/fixtures/complex_before.json', './tests/fixtures/complex_after.json') + '\n'

