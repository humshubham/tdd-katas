import pytest 

from app import convert

def test_convert_one():
    assert convert(1) == "I"

def test_convert_two():
    assert convert(2) == "II"

def test_convert_three():
    assert convert(3) == "III"

def test_convert_four():
    assert convert(4) == "IV"

def test_convert_five():
    assert convert(5) == "V"

def test_convert_nine():
    assert convert(9) == "IX"

def test_convert_ten():
    assert convert(10) == "X"

def test_convert_eleven():
    assert convert(11) == "XI"

def test_convert_twenty():
    assert convert(20) == "XX"

def test_convert_fifty():
    assert convert(50) == "L"

def test_convert_eighty():
    assert convert(80) == "LXXX"

def test_convert_ninety():
    assert convert(90) == "CM"

def test_convert_hundred():
    assert convert(100) == "C"

def test_convert_four_hundred():
    assert convert(400) == "CD"

def test_convert_five_hundred():
    assert convert(500) == "D"

def test_convert_eight_hundred():
    assert convert(800) == "DCCC"

def test_convert_nine_hundred():
    assert convert(900) == "CM"

def test_convert_thousand():
    assert convert(1000) == "M"

