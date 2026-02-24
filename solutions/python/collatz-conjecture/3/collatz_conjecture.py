# A function to test the Collatz Conjecture for any given number and return the number of steps
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    if number == 1:
        return counter
    while number != 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        counter += 1
    return counter          