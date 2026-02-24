def primes(limit: int) -> list[int]:
    '''Create a list of prime numbers up to a given limit using the Sieve of Eratosthenes.'''

    # Initialize the sieve with True for all numbers from 2 to limit
    sieve = [True] * (limit + 1)

    # Main sieve loop
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as not prime
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

    # Return the list of primes
    return [num for num in range(2, limit + 1) if sieve[num]]
