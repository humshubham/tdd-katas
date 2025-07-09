import pytest

from app import is_password_valid

def test_len_less_than_equal_to_eight():
    assert is_password_valid("12345678") == False