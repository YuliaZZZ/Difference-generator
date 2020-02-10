# -*- coding:utf-8 -*-
import pytest
from gen_diff import generate_diff


file = open('./tests/fixtures/result.txt', 'r')
answer = file.read()


file2 = open('./tests/fixtures/result2.txt', 'r')
answer2 = file2.read()

def test_answer():
    assert answer == generate_diff.engine('./tests/fixtures/before.json', './tests/fixtures/after.json')
    assert answer2 == generate_diff.engine('./tests/fixtures/before_empty.json', './tests/fixtures/after_empty.json')

