def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 or number % 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = set() #create an empty set for the factors
    
    for i in range(1,int((number**0.5)//1)+1): #only check numbers up to the square root rounded up
        factors.add(i if not number % i else 1) #add i if it's a factor
        factors.add(int(number / i) if not number % i else 1) #add number/i if it's a factor
        factors.discard(number) #remove the original number from the set
    
    aliquot_sum = sum(factors) #calculate the aliquot sum
    
    if number < aliquot_sum: return 'abundant'
    if number > aliquot_sum: return 'deficient'
    if number == aliquot_sum: return 'perfect'
