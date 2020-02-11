# -*- coding:utf-8 -*-
import pytest
import yaml
from gen_diff import generate_diff, parsers


file = open('./tests/fixtures/result.txt', 'r')
answer = file.read()


file2 = open('./tests/fixtures/result2.txt', 'r')
answer2 = file2.read()


def test_answer():
    assert answer == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json')
    assert answer2 == generate_diff.engine('./tests/fixtures/before_empty.json', './tests/fixtures/after_empty.json')
    assert yaml.safe_load(open('./tests/fixtures/before.yml')) == parsers.parser('./tests/fixtures/before.yml')
    assert type(generate_diff.engine('./tests/fixtures/before.yml', './tests/fixtures/after.yml')) is str
