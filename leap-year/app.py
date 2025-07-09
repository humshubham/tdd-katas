def is_leap_year(year:int) -> bool:
    if year%100 == 0:
        if year%400 != 0:
            return False
        return True
    return year % 4 == 0