ALLERGENS = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats']

class Allergies:
    
    def __init__(self, score):
        self.lst = [allergen for i,allergen in enumerate(ALLERGENS) if score & (1 << i)]

    def allergic_to(self, item):
        return item in self.lst
