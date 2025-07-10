import pytest

from app import print_christmas_song

def test_less_than_one():
    with pytest.raises(Exception) as e:
        print_christmas_song(0)
    assert "Day should be from 1 to 12" in str(e)

def test_more_than_twelve():
    with pytest.raises(Exception) as e:
        print_christmas_song(13)
    assert "Day should be from 1 to 12" in str(e)

def test_day_one():
    assert   print_christmas_song(1) == "On the First day of Christmas,\nMy true love gave to me:\nA partridge in a pear tree"