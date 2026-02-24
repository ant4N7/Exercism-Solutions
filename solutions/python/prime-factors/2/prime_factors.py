def factors(n: int) -> list[int]:
    factors = []
    
    while not n%2:
        factors += [2]
        n //= 2
        
    for i in range(3,int(n**.5)+1,2):
        while not n%i:
            factors += [i]
            n //= i
            
    if n>2: factors += [n]
        
    return factors
