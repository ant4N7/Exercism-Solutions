def square_root(number: int) -> int:
    #a binary estimate within 1 iteration of sqrt(number)
    estimate = 1 << ((len(bin(number))-2) >> 1)
    #one iteration of Newton's method
    estimate = (estimate + (number//estimate)) >> 1
    return estimate
