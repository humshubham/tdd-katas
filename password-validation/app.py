def is_password_valid(password:str)->bool:
    is_valid_len = len(password) > 8
 
    has_capital_letter = False   
    for char in password:
        if char.isupper():
            has_capital_letter = True
            break
    
    return is_valid_len and has_capital_letter