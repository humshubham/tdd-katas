import pytest

from app import PasswordValidator

def test_len_less_than_equal_to_eight():
    assert PasswordValidator("12345678").is_password_valid() == False

def test_does_not_contain_capital_letter():
    assert PasswordValidator("lowercase").is_password_valid() == False

def test_does_not_contain_lowercase_letter():
    assert PasswordValidator("UPPERCASE").is_password_valid() == False

def test_does_not_contain_number():
    assert PasswordValidator("noNumbers").is_password_valid() == False

def test_does_not_contain_underscore():
    assert PasswordValidator("noUnderScore1").is_password_valid() == False

def test_valid_password():
    assert PasswordValidator("noUnderScore1_").is_password_valid() == True