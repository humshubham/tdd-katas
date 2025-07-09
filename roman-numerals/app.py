def convert(number:int)->str:
    roman_str = ""
    unique_nums_dict = {
        1000:"M", 500:"D", 100:"C", 50:"L", 10:"X",
        9:"IX", 5:"V", 4:"IV", 3:"III", 2:"II", 1:"I"
    }
    unique_nums = list(unique_nums_dict.keys())
    
    position = 0
    while number >= 0 and position < len(unique_nums):
        current_number = unique_nums[position]
        if number - current_number >= 0:
            
            number-=current_number
            roman_str+=unique_nums_dict[current_number]
        if number < current_number:
            position +=1

    return roman_str