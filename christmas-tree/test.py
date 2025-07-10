import pytest

from app import print_christmas_tree

def test_height_zero():
    with pytest.raises(Exception) as e:
        print_christmas_tree(0)
    assert "Height can not be less than two" in str(e.value)

def test_height_one():
    with pytest.raises(Exception) as e:
        print_christmas_tree(1)
    assert "Height can not be less than two" in str(e.value)

def test_height_two():
    assert print_christmas_tree(2) == """ X\nXXX\n |"""

def test_height_three():
    assert print_christmas_tree(3) == """  X\n XXX\nXXXXX\n  |"""

def test_height_four():
    assert print_christmas_tree(4) == """   X\n  XXX\n XXXXX\nXXXXXXX\n   |"""

def test_height_ten():
    assert print_christmas_tree(10) == """         X\n        XXX\n       XXXXX\n      XXXXXXX\n     XXXXXXXXX\n    XXXXXXXXXXX\n   XXXXXXXXXXXXX\n  XXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXX\n         |"""
