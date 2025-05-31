import pytest 

from chop import chop

def test_chop_not_found_returns_negative_one_empty():
    assert chop(3, []) == -1

def test_chop_not_found_returns_negative_one():
    assert chop(3, [1]) == -1

def test_chop_found_returns_position():
    assert chop(1, [1]) == 0

def test_chop_found_returns_position_multi_elements():
    assert chop(1, [1, 3, 5]) == 0
    assert chop(3, [1, 3, 5]) == 1
    assert chop(5, [1, 3, 5]) == 2

def test_chop_not_found_returns_negative_one_multi_elements():
    assert chop(0, [1, 3, 5]) == -1
    assert chop(2, [1, 3, 5]) == -1
    assert chop(4, [1, 3, 5]) == -1
    assert chop(6, [1, 3, 5]) == -1

def test_chop_found_returns_position_long_list():
  assert chop(1, [1, 3, 5, 7]) == 0
  assert chop(3, [1, 3, 5, 7]) == 1
  assert chop(7, [1, 3, 5, 7]) == 3
  assert chop(5, [1, 3, 5, 7]) == 2


def test_chop_not_found_returns_negative_long_list():
  assert chop(0, [1, 3, 5, 7]) == -1
  assert chop(2, [1, 3, 5, 7]) == -1
  assert chop(4, [1, 3, 5, 7]) == -1
  assert chop(6, [1, 3, 5, 7]) == -1
  assert chop(8, [1, 3, 5, 7]) == -1
