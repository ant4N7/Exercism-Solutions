class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')

    def valid(self):
        card_num = self.card_num
        if len(card_num) <= 1 or not card_num.isdecimal():
            return False

        res = [int(i) for i in card_num]
        res[-2::-2] = [2*i - 9*(i>4) for i in res[-2::-2]]

        return not (sum(res)%10)
        
        