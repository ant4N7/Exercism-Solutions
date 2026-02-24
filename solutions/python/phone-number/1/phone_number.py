import re

class PhoneNumber:
    
    pattern = r'^\D*(\d*)\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*$'

    def __init__(self, number):
        self.validate(number)
        self.number = re.sub(self.pattern,r'\2\3\4',number)
        self.area_code = re.search(r'\d{3}',number)[0]
        self.country_code = re.sub(self.pattern,r'\1',number)

    @staticmethod
    def validate(number):
        errors = ['letters not permitted','punctuations not permitted',
                  'must not be fewer than 10 digits','11 digits must start with 1',
                  'must not be greater than 11 digits','area code cannot start with zero',
                  'area code cannot start with one','exchange code cannot start with zero',
                  'exchange code cannot start with one']
        has_letters = [m[0] for m in re.finditer(r'[a-zA-Z]',number)]
        has_punctuation = [m[0] for m in re.finditer(r'[!@#$%^&*]',number)]
        digits = [m[0] for m in re.finditer(r'\d',number)]
        if has_letters: raise ValueError(errors[0])
        if has_punctuation: raise ValueError(errors[1])
        if len(digits) < 10: raise ValueError(errors[2])
        if len(digits) == 11 and digits[0] != '1': raise ValueError(errors[3])
        if len(digits) > 11: raise ValueError(errors[4])
        if digits[-10] == '0': raise ValueError(errors[5])
        if digits[-10] == '1': raise ValueError(errors[6])
        if digits[-7] == '0': raise ValueError(errors[7])
        if digits[-7] == '1': raise ValueError(errors[8])

    def pretty(self):
        return re.sub(self.pattern,r'(\2)-\3-\4',self.number)
