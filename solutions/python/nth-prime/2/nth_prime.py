def prime(number: int) -> int:
    if number < 1: raise ValueError('there is no zeroth prime')
    primes = [2,3]
    
    n=3
    while len(primes)<number:
        n+=2
        if all(n%p for p in primes):
            primes.append(n)

    return primes[number-1]
