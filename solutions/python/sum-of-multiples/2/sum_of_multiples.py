def sum_of_multiples(level, base_values):
    unique_multiples = set()
    for value in base_values:
        if value > 0:
            unique_multiples |= {i for i in range(value,level,value)}
    return sum(unique_multiples)
