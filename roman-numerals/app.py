def convert(number:int)->str:
    roman_str = ""
    unique_nums_dict = {
        1000:"M", 500:"D", 100:"C", 50:"L", 10:"X",
        5:"V",4:"IV",3:"III",2:"II",1:"I"
    }
    unique_nums = list(unique_nums_dict.keys())
    
    position = 0
    while number >= 0 and position < len(unique_nums):

        if number - unique_nums[position] >= 0:
            
            number-=unique_nums[position]
            roman_str+=unique_nums_dict[unique_nums[position]]

        position +=1

    return roman_str