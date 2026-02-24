def is_palindrome(product):
    return product == product[::-1]

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
    value = None
    factors = []
    for i in range(max_factor,min_factor-1,-1):
        for j in range(max_factor,i-1,-1):
            product = i*j
            if value is not None and product < value:
                break
            if is_palindrome(str(product)):
                if value is None or product > value:
                    value = product
                    factors = [(i,j)]
                elif product == value:
                    factors.append((i,j))
    return (value,factors)

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
    value = None
    factors = []
    for i in range(min_factor,max_factor+1):
        for j in range(i,max_factor+1):
            product = i*j
            if value is not None and product > value:
                break
            if is_palindrome(str(product)):
                if value is None or product < value:
                    value = product
                    factors = [(i,j)]
                elif product == value:
                    factors.append((i,j))
    return (value,factors)    
