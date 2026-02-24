def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """convert a list of digits in a given input base to a list of digits in the given output base"""

    #input validation and converting to base 10
    if input_base < 2: raise ValueError('input base must be >= 2')
    if output_base < 2: raise ValueError('output base must be >= 2')
    base_ten = 0
    for i,d in zip(range(len(digits)-1,-1,-1),digits):
        if not 0<=d<input_base: raise ValueError('all digits must satisfy 0 <= d < input base')
        base_ten += d*input_base**i

    #early return for 0 and empty lists
    if not base_ten: return [0]
    
    #main logic
    result = []
    while base_ten:
        result.insert(0, base_ten % output_base)
        base_ten //= output_base
    return result
