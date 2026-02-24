def get_number_of_digits(number):
    """returns the number of digits in the number.
    
    param :: number :: int - the number being tested.
    return :: number_of_digits:: int - how many digits are in the number being tested.
    """
    temp = number
    number_of_digits = 0
    while temp != 0:
        temp = temp // 10
        number_of_digits += 1
    return number_of_digits

def do_math(number):
    """does the heavy lifting 
    
    param :: number :: int - the number being tested
    return :: sum :: int - sum of each digit raised to the power of the number of digits
    """
    sum = 0
    temp2 = number
    for digit in range(get_number_of_digits(number)):
        sum = ((temp2 % 10) ** get_number_of_digits(number)) + sum
        temp2 = temp2 // 10
    return sum

    
def is_armstrong_number(number):
    
    if get_number_of_digits(number) == 1:
        return True
    elif get_number_of_digits(number) == 2:
        return False
    else:
        return number == do_math(number)
    