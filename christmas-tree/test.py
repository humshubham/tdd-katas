import pytest

from app import print_christmas_tree

def test_heigh_zero():
    with pytest.raises(Exception) as e:
        print_christmas_tree(0)
    assert "Height can not be less than one" in str(e.value)