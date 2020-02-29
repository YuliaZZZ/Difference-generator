# -*- coding:utf-8 -*-
import pytest
import yaml
from gen_diff import generate_diff, parsers
from gen_diff.formatters import plain, str_dict, to_json


def  reader(file):
    with open(file, 'r') as input_file:
        answer = input_file.read()
    return answer


def test_answer():
    assert reader('./tests/fixtures/result.txt') == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json', str_dict.to_format)
    assert yaml.safe_load(open('./tests/fixtures/before.yml')) == parsers.parser('./tests/fixtures/before.yml')
    assert isinstance(generate_diff.engine('./tests/fixtures/before.yml', './tests/fixtures/after.yml', str_dict.to_format), str)
    assert reader('./tests/fixtures/recursion_result.txt') == generate_diff.engine('./tests/fixtures/complex_before.json', './tests/fixtures/complex_after.json', str_dict.to_format)
    assert reader('./tests/fixtures/text_result.txt') == generate_diff.engine('./tests/fixtures/complex_before.json', './tests/fixtures/complex_after.json', plain.to_format)
    assert reader('tests/fixtures/json_result.json') == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json', to_json.to_format)
