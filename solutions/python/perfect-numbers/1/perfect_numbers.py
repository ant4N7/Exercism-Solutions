def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 or number % 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = set()
    for i in range(int((number**0.5)//1)+1):
        factors.add(int(number / (i+1)) if not number % (i+1) else 1)
        factors.add(i+1 if not number % (i+1) else 1)
        factors.discard(number)
    aliquot_sum = sum(factors)
    if number < aliquot_sum: return 'abundant'
    if number > aliquot_sum: return 'deficient'
    if number == aliquot_sum: return 'perfect'
