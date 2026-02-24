NUM_DICT = {(' _ ', '| |', '|_|', '   '):'0',('   ', '  |', '  |', '   '):'1',
            (' _ ', ' _|', '|_ ', '   '):'2',(' _ ', ' _|', ' _|', '   '):'3',
            ('   ', '|_|', '  |', '   '):'4',(' _ ', '|_ ', ' _|', '   '):'5',
            (' _ ', '|_ ', '|_|', '   '):'6',(' _ ', '  |', '  |', '   '):'7',
            (' _ ', '|_|', '|_|', '   '):'8',(' _ ', '|_|', ' _|', '   '):'9'}


def convert(input_grid: list[str]) -> str:
    
    #reject invalid input formats
    if len(input_grid) % 4:
        raise ValueError('Number of input lines is not a multiple of four')
    if any(len(col) % 3 for col in input_grid):
        raise ValueError('Number of input columns is not a multiple of three')

    #split lines of digits into groups
    inputs = [input_grid[i:i+4] for i in range(0,len(input_grid),4)]

    #build list of processed ODR numbers
    results = []
    for input in inputs:
        results.append(process_input(input))
    
    return ','.join(results)

def process_input(input: list[str]) -> str:
    '''function to convert single lines of OCR numbers'''
    
    #build a stack of len 3 strings
    stack = [line[i:i+3] for line in input for i in range(0,len(line),3)]
    
    #reorder and group stack into NUM_DICT keys
    step = len(input[0])//3   #step is the number of digits in the input
    stack = [stack[i::step] for i in range(len(stack)//4)]

    #process the stack
    acc = ''
    while stack:
        acc += NUM_DICT.get(tuple(stack.pop(0)),'?')

    return acc
