class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_password_valid(self)->bool:
        is_valid_len = len(self.password) > 8
    
        has_capital_letter = False  
        has_lowercase_letter = False 
        has_a_number = False
        has_an_underscore = False

        for char in self.password:
            if char.isupper():
                has_capital_letter = True
            elif char.islower():
                has_lowercase_letter = True
            elif char.isdigit():
                has_a_number = True
            elif char == "_":
                has_an_underscore = True
        
        return is_valid_len and has_capital_letter and has_lowercase_letter and has_a_number and has_an_underscore