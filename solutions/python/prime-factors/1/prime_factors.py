def factors(n):
    upper_range = int(n**.5)+1

    def _factor(n, acc=[]):
        for i in range(2,upper_range):
            if not n%i:
                return _factor(n//i, acc+[i])
        if n > 1:
            acc.append(n)
        return acc

    return _factor(n)
