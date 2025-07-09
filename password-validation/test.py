import pytest

from app import is_password_valid

def test_len_less_than_equal_to_eight():
    assert is_password_valid("12345678") == False

def test_does_not_contain_capital_letter():
    assert is_password_valid("lowercase") == False

def test_does_not_contain_lowercase_letter():
    assert is_password_valid("UPPERCASE") == False

def test_does_not_contain_number():
    assert is_password_valid("noNumbers") == False