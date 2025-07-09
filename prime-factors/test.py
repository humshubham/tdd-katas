import pytest 

from app import prime_factors

def test_factors_of_one():
    assert(prime_factors(1)) == []

def test_factors_of_two():
    assert(prime_factors(2)) == [2]

def test_factors_of_three():
    assert(prime_factors(3)) == [3]

def test_factors_of_four():
    assert(prime_factors(4)) == [2, 2]

def test_factors_of_five():
    assert(prime_factors(5)) == [5]

def test_factors_of_six():
    assert(prime_factors(6)) == [2, 3]

def test_factors_of_seven():
    assert(prime_factors(7)) == [7]

def test_factors_of_eight():
    assert(prime_factors(8)) == [2,2,2]