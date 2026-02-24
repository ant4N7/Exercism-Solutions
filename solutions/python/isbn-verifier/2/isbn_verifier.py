def is_valid(isbn):
    '''
    :param isbn: string - representing an ISBN number to test
    :return: bool - if the string of digits represents a valid ISBN
    '''
    
    #remove hyphens and capitalize letters
    isbn = isbn.replace('-', '').upper() 
    
    #check if the string is in the correct length
    if len(isbn) != 10: return False

    #sum the weighted digits and return false if they are not digits
    weighted_sum = 0 
    for index, digit in enumerate(isbn[0:9]): 
        if not digit.isdigit(): return False
        weighted_sum += int(digit) * (10 - index)

    #evaluate the check digit
    if isbn[-1] == 'X': weighted_sum += 10
    elif isbn[-1].isdigit(): weighted_sum += int(isbn[-1])
    else: return False

    return weighted_sum % 11 == 0
