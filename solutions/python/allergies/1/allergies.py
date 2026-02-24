class Allergies:
    ALLERGENS = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats']
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if item not in self.ALLERGENS: return False
        item_index = self.ALLERGENS.index(item)
        return bool(self.score & (1 << item_index))

    @property
    def lst(self):
        return [allergen for i, allergen in enumerate(self.ALLERGENS) if self.score & (1 << i)]
