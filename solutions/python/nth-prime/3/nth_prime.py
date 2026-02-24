def prime(number):
    if number == 0: raise ValueError('there is no zeroth prime')
    if 1<=number<3: return number+1
    prime = 3
    counter = 1
    while counter<number:
        for trial in range(3, int(prime ** 0.5) + 1, 2):
            if not prime % trial: break
        else: counter += 1
        if counter < number: prime += 2
    return prime
    