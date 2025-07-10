def print_christmas_song(day:int)->str:
    if day < 1 or day > 12:
        raise Exception("Day should be from 1 to 12")
    return "On the First day of Christmas,\nMy true love gave to me:\nA partridge in a pear tree"