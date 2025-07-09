import pytest

from app import convert

def test_convert_one():
    assert convert(1) == "1"

def test_convert_two():
    assert convert(2) == "2"

def test_convert_three():
    assert convert(3) == "Fizz"

def test_convert_four():
    assert convert(4) == "4"

def test_convert_five():
    assert convert(5) == "Buzz"

def test_convert_nine():
    assert convert(9) == "Fizz"

def test_convert_ten():
    assert convert(10) == "Buzz"

def test_convert_fifteen():
    assert convert(15) == "FizzBuzz"