def square_root(number):
    estimate = number
    for _ in range(10):
        estimate = (estimate + (number/estimate))*.5
    return int(estimate)
