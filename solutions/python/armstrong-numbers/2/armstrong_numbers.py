def is_armstrong_number(number: int) -> bool:
    
    # convert the number to a string
    number_string = str(number)
    
    # use the string to generate the individual digits
    digits = (int(digit) for digit in number_string)
    
    # use the string to count the number of digits
    digit_count = len(number_string)
    
    # add up each digit to the power of the number of digits
    total = sum(digit**digit_count for digit in digits)
    
    return total == number
