def convert(number:int)->str:
    roman_str = ""

    value_map = [
        (1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"CM"), (50,"L"), 
        (40,"XC"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (3,"III"), (2,"II"), (1,"I")
    ]

    for num, value in value_map:
        while number-num>=0:
            number-=num
            roman_str+=value

    return roman_str