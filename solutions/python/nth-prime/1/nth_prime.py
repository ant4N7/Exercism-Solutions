def prime(number: int) -> int:
    if number < 1: raise ValueError('there is no zeroth prime')
    primes = [2,3]
    
    def _prime_generator():
        n=primes[-1]
        while True:
            n+=2
            if all(n%p for p in primes):
                primes.append(n)
                yield 

    for _ in range(number-2): next(_prime_generator())
    return primes[number-1]
