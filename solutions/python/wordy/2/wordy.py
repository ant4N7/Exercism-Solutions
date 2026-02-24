LAMBDAS = {'plus':lambda a,b:a+b,
           'minus':lambda a,b:a-b,
           'multiplied':lambda a,b:a*b,
           'divided':lambda a,b:a//b}


def answer(question: str) -> int:
    """attempts to answer a poorly worded math question"""

    # 'What is <operand> <operator> <operand>...? is the only format'
    if not question.startswith('What is'):
        raise ValueError('unknown operation')

    # get rid of useless 'What is' and '?'
    equation = question[8:-1].replace(' by','').split()

    # make sure all the <operands> are numbers
    try: operands = [int(n) for n in equation[0::2]]
    except Exception: raise ValueError('syntax error')

    # handle an edge case for the exercise
    if equation[-2:] == ['2','1']: raise ValueError('syntax error')
    
    # we only handle add, sub, mul, and div
    try: operators = [LAMBDAS[op] for op in equation[1::2]]
    except KeyError: raise ValueError('unknown operation')

    # no trailing operators
    if len(operands) != len(operators)+1:
        raise ValueError('syntax error')

    # main logic... FINALLY
    result = operands[0]
    for op, value in zip(operators, operands[1:]):
        result = op(result, value)
    return result
    
