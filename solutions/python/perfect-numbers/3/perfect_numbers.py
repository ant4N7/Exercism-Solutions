def classify(number):
    #A perfect number equals the sum of its positive divisors.
    aliquot_sum = sum([i for i in range(1, number) if number % i == 0])
    if number == aliquot_sum and number != 0: return 'perfect'
    if 1 < number < aliquot_sum: return 'abundant'
    if number > aliquot_sum: return 'deficient'
    raise ValueError("Classification is only possible for positive integers.")
