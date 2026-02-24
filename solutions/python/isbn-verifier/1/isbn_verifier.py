def is_valid(isbn):
    '''
    :param isbn: string - representing an ISBN number to test
    :return: bool - if the string of digits represents a valid ISBN
    '''
    
    list_digits = list(isbn.replace('-', '')) #remove hyphens and put the digits in a list
    
    #check if the string is in the correct format
    if len(list_digits) != 10: return False
    test_digits = '0123456789'
    test_check = '0123456789X'
    for digit in list_digits[:-1]: 
        if digit not in test_digits: return False
    if list_digits[-1] not in test_check: return False
    
    if list_digits[-1] == 'X': list_digits[-1] = '10' #replace an 'x' with '10'

    list_integers = [int(digit) for digit in list_digits] #convert list of strings to list of ints

    first_calc = 0 #initialize variable to hold the first calculation

    #calculate 10d₁ + 9d₂ + 8d₃ + 7d₄ + 6d₅ + 5d₆ + 4d₇ + 3d₈ + 2d₉ + d₁₀
    for i in range(10):
        first_calc += list_integers[0] * len(list_integers)
        list_integers.pop(0)

    return first_calc % 11 == 0
