import pytest 

from app import is_leap_year

def test_not_divisible_by_4():
    assert is_leap_year(2001) == False

def test_divisible_by_4():
    assert is_leap_year(2004) == True

def test_not_divisible_by_400():
    assert is_leap_year(1967) == False

def test_divisible_by_400():
    assert is_leap_year(1600) == True

def test_divisible_by_100_not_400():
    assert is_leap_year(1800) == False

def test_divisible_by_100_and_400():
    assert is_leap_year(2000) == True