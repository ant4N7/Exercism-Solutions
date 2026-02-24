def primes(limit: int) -> list[int]:
    '''create a list of numbers from 2 up to a given limit and mark them prime or not prime'''

    #initialize the sieve with positive ints from 2 up to the limit with default value 'unmarked'
    sieve = dict.fromkeys(range(2,limit+1),'unmarked')

    #a helper function that finds the first 'unmarked' value in the list
    def first_unmarked(sieve: dict[int:str]) -> int:
        for key in sieve.keys():
            if sieve[key] == 'unmarked':
                return key

    #loop through the list until all ints are marked prime or not prime
    while 'unmarked' in sieve.values():
        multiples = first_unmarked(sieve)
        sieve[first_unmarked(sieve)] = 'prime'
        for n in range(multiples**2,limit+1,multiples):
            sieve[n] = 'not prime'

    #for this exercise we return a list of the ints that have been marked 'prime'
    return [key for key in sieve.keys() if sieve[key] == 'prime']
