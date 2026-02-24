def egg_count(display_value):
    # if not display_value: return 0
    # if not (display_value & (display_value - 1)): return 1
    return str(bin(display_value)).count('1')
