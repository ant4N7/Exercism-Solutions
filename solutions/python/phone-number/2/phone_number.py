import re

class PhoneNumber:
    
    pattern = r'^\D*(\d*)\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*$'
    errors = {'letters':'letters not permitted',
              'punctuations':'punctuations not permitted',
              'NEN':'must not be fewer than 10 digits',
              'notUS':'11 digits must start with 1',
              'too long':'must not be greater than 11 digits',
              'area0':'area code cannot start with zero',
              'area1':'area code cannot start with one',
              'ex0':'exchange code cannot start with zero',
              'ex1':'exchange code cannot start with one'}

    def __init__(self, number: str):
        self.validate(number)
        self.number = re.sub(self.pattern,r'\2\3\4',number)
        self.area_code = re.search(r'\d{3}',number)[0]

    @classmethod
    def validate(cls,number: str):
        digits = [m[0] for m in re.finditer(r'\d',number)]
        if re.search(r'[a-zA-Z]',number): raise ValueError(cls.errors['letters'])
        if re.search(r'[!@#$%^&*]',number): raise ValueError(cls.errors['punctuations'])
        if len(digits) < 10: raise ValueError(cls.errors['NEN'])
        if len(digits) == 11 and digits[0] != '1': raise ValueError(cls.errors['notUS'])
        if len(digits) > 11: raise ValueError(cls.errors['too long'])
        if digits[-10] == '0': raise ValueError(cls.errors['area0'])
        if digits[-10] == '1': raise ValueError(cls.errors['area1'])
        if digits[-7] == '0': raise ValueError(cls.errors['ex0'])
        if digits[-7] == '1': raise ValueError(cls.errors['ex1'])

    def pretty(self) -> str:
        return re.sub(self.pattern,r'(\2)-\3-\4',self.number)
