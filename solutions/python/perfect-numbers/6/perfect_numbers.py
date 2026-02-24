def classify(n):
    if n < 1: raise ValueError("Classification is only possible for positive integers.")
    a = sum(i for i in range(1, n//2+1) if not n % i)
    return ['deficient','perfect','abundant'][(n<a)-(n>a)+1]