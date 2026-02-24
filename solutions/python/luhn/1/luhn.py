class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')

    def valid(self):
        
        #skip strings containing non numbers or too short
        if not self.card_num.isdecimal() or len(self.card_num)<=1:
            return False
        
        #calculate the sum for Luhn algorithm
        sum = 0
        parity = len(self.card_num) % 2
        for i in range(len(self.card_num)):
            if i % 2 != parity:
                sum += int(self.card_num[i])
            elif int(self.card_num[i]) > 4:
                sum += 2 * int(self.card_num[i]) - 9
            else:
                sum += 2 * int(self.card_num[i])

        #checks if s mod 10 == 0 instead of (10-(s mod 10)) mod 10 == check digit
        return not sum%10
        