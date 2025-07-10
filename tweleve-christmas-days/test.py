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
    assert print_christmas_song(1).lower() == "On the First day of Christmas,\nMy true love gave to me:\nA partridge in a pear tree.".lower()

def test_day_two():
    assert print_christmas_song(2).lower() == "On the Second day of Christmas,\nMy true love gave to me:\nTwo turtle doves,\nAnd a partridge in a pear tree.".lower()

def test_day_five():
    assert print_christmas_song(5).lower() == "On the fifth day of Christmas,\nMy true love gave to me:\nFive golden rings,\nFour calling birds,\nThree French hens,\nTwo turtle doves,\nAnd a partridge in a pear tree.".lower()

def test_day_twelve():
    assert print_christmas_song(12).lower() == "On the twelfth day of Christmas,\nMy true love gave to me:\nTwelve drummers drumming,\nEleven pipers piping,\nTen lords a-leaping,\nNine ladies dancing,\nEight maids a-milking,\nSeven swans a-swimming,\nSix geese a-laying,\nFive golden rings,\nFour calling birds,\nThree French hens,\nTwo turtle doves,\nAnd a partridge in a pear tree.".lower()