def print_christmas_song(day:int)->str:
    if day < 1 or day > 12:
        raise Exception("Day should be from 1 to 12")
    
    day_ordinal = {
        1: "First", 2: "Second", 3: "Third", 4: "Fourth",
        5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth",
        9: "Ninth", 10: "Tenth", 11: "Eleventh", 12: "Twelfth"
    }

    day_gifts = [
        "Twelve drummers drumming",
        "Eleven pipers piping",
        "Ten lords a-leaping",
        "Nine ladies dancing",
        "Eight maids a-milking",
        "Seven swans a-swimming",
        "Six geese a-laying",
        "Five golden rings",
        "Four calling birds",
        "Three French hens",
        "Two turtle doves",
        "a partridge in a pear tree"
    ]

    christmas_song = f"On the {day_ordinal[day]} day of Christmas,\nMy true love gave to me:\n"
    applicable_gifts = day_gifts[12-day:]

    
    if day>1:
        christmas_song+=",\n".join(applicable_gifts[:-1])
        christmas_song += f",\nAnd {applicable_gifts[-1]}."
    else:
        christmas_song+=f"{applicable_gifts[0]}."

    return christmas_song
