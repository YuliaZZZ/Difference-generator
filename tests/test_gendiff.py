# -*- coding:utf-8 -*-
import pytest
import yaml
from gen_diff import engine, parsers
from gen_diff.formatters import json_view, str_view, text_view


def readed(file):
    with open(file, 'r') as input_file:
        answer = input_file.read()
    return answer


def test_answer():
    assert readed('./tests/fixtures/result.txt') == engine.generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        str_view.make_format
    )
    assert yaml.safe_load(open('./tests/fixtures/before.yml')) == parsers.parsed('./tests/fixtures/before.yml')
    assert isinstance(engine.generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml',
        str_view.make_format), str
    )
    assert readed('./tests/fixtures/recursion_result.txt') == engine.generate_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        str_view.make_format
    )
    assert readed('./tests/fixtures/text_result.txt') == engine.generate_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        text_view.make_format
    )
    assert readed('tests/fixtures/json_result.json') == engine.generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        json_view.make_format
    )
