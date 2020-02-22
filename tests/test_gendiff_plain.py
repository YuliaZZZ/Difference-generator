# -*- coding:utf-8 -*-
import pytest
import yaml
from gen_diff import generate_diff, parsers
from gen_diff.formatters import plain, str_dict, to_json


file = open('./tests/fixtures/result.txt', 'r')
answer = file.read()


file1 = open('./tests/fixtures/recursion_result.txt', 'r')
answer2 = file1.read()


file2 = open('./tests/fixtures/text_result.txt', 'r')
answer3 = file2.read()


file3 = open('tests/fixtures/json_result.json', 'r')
answer4 = file3.read()


def test_answer():
    assert answer == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json', str_dict.to_format) + '\n'
    assert yaml.safe_load(open('./tests/fixtures/before.yml')) == parsers.parser('./tests/fixtures/before.yml')
    assert type(generate_diff.engine('./tests/fixtures/before.yml', './tests/fixtures/after.yml', str_dict.to_format)) is str
    assert answer2 == generate_diff.engine('./tests/fixtures/complex_before.json', './tests/fixtures/complex_after.json', str_dict.to_format) + '\n'
    assert answer3 == generate_diff.engine('./tests/fixtures/complex_before.json', './tests/fixtures/complex_after.json', plain.to_format)
    assert answer4 == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json', to_json.to_format) + '\n'
