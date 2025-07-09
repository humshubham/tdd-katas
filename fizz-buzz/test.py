import pytest

from app import convert

def test_convert_one():
    assert convert(1) == "1"

def test_convert_two():
    assert convert(2) == "2"

def test_convert_three():
    assert convert(3) == "Fizz"