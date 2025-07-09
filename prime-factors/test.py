import pytest 

from app import prime_factors

def test_factors_of_one():
    assert(prime_factors(1)) == []

def test_factors_of_two():
    assert(prime_factors(2)) == [2]