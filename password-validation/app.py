class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_valid_length(self, length:int)->bool:
        return len(self.password) > length
    
    def has_capital_letter(self)->bool:
        return any(char.isupper() for char in self.password)
    
    def has_lower_letter(self)->bool:
        return any(char.islower() for char in self.password)
    
    def has_number(self)->bool:
        return any(char.isdigit() for char in self.password)
    
    def has_underscore(self)->bool:
        return "_" in self.password
    
    def is_password_valid(self)->bool:

        return (
            self.is_valid_length(8) and
            self.has_capital_letter() and 
            self.has_lower_letter() and 
            self.has_number() and 
            self.has_underscore()
                ) 