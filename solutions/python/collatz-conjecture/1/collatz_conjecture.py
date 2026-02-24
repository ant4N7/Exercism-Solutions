# A function to test the Collatz Conjecture for any given number
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    i = 0
    if number == 1:
        return i
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            i = i + 1
        else:
            number = (number * 3) + 1
            i = i + 1
    return i            