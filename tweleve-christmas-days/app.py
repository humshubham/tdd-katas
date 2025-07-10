def print_christmas_song(day:int)->str:
    if day < 1 or day > 12:
        raise Exception("Day should be from 1 to 12")
    
    day_counter=day
    
    match day:
        case 1:
            day_str="First"
        case 2:
            day_str="Second"
        case 3:
            day_str="Third"
        case 4:
            day_str="Fourth"
        case 5:
            day_str="Fifth"
        case 6:
            day_str="Sixth"
        case 7:
            day_str="Seventh"
        case 8:
            day_str="Eighth"
        case 9:
            day_str="Ninth"
        case 10:
            day_str="Tenth"
        case 11:
            day_str="Eleventh"
        case 12:
            day_str="Twelfth"

    day_gift_map=[
        (12,"Twelve drummers drumming"),
        (11,"Eleven pipers piping"),
        (10,"Ten lords a-leaping"),
        (9,"Nine ladies dancing"),
        (8,"Eight maids a-milking"),
        (7,"Seven swans a-swimming"),
        (6,"Six geese a-laying"),
        (5,"Five golden rings"),
        (4,"Four calling birds"),
        (3,"Three French hens"),
        (2,"Two turtle doves"),
        (1,"a partridge in a pear tree")
    ]

    christmas_song = f"On the {day_str} day of Christmas,\nMy true love gave to me:\n"

    for day_num, gift in day_gift_map:
        if day_counter == day_num:
            if day>1 and day_num==1:
                christmas_song+=f"And {gift}."
            elif day==1 and day_num==1:
                christmas_song+=f"{gift}."
            else:
                christmas_song+=f"{gift},\n"
                day_counter-=1

    return christmas_song
