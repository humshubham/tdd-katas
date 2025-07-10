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
