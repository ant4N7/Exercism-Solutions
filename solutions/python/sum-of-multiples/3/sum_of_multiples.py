def sum_of_multiples(level, base_values):
    return sum({i for value in base_values if value > 0 for i in range(value, level, value)})
