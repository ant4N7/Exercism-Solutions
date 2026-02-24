def sum_of_multiples(level, base_values):
    unique_multiples = set()
    for value in base_values:
        unique_multiples |= {value*i for i in range(1,level) if value*i < level}
    return sum(unique_multiples)
