# -*- coding:utf-8 -*-
import pytest
from gen_diff import generate_diff


file = open('./tests/fixtures/result.txt', 'r')
answer = file.read()


def test_answer():
    assert answer == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json')
