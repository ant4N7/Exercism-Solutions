NUM_DICT = {(' _ ', '| |', '|_|', '   '):'0',('   ', '  |', '  |', '   '):'1',
            (' _ ', ' _|', '|_ ', '   '):'2',(' _ ', ' _|', ' _|', '   '):'3',
            ('   ', '|_|', '  |', '   '):'4',(' _ ', '|_ ', ' _|', '   '):'5',
            (' _ ', '|_ ', '|_|', '   '):'6',(' _ ', '  |', '  |', '   '):'7',
            (' _ ', '|_|', '|_|', '   '):'8',(' _ ', '|_|', ' _|', '   '):'9'}


def convert(input_grid):

    #reject invalid input formats
    if len(input_grid) % 4:
            raise ValueError('Number of input lines is not a multiple of four')
    for ish in input_grid:
        if len(ish) % 3:
            raise ValueError('Number of input columns is not a multiple of three')

    #split lines of digits into groups
    input_stack = [input_grid[i:i+4] for i in range(0,len(input_grid),4)]

    #function to process inputs
    def process_input(input):
        #build a number stack
        stack = []
        for line in input:
            for i in range(0,len(line),3):
                stack.append(line[i:i+3])
        step = len(input[0])//3
        stack = [stack[i::step] for i in range(len(stack)//4)]
        
        #dict lookup helper function
        def one_digit(digit):
            
            if tuple(digit) not in NUM_DICT:
                return '?'
            return NUM_DICT[tuple(digit)]
    
        #process the stack
        acc = ''
        while stack:
            acc += one_digit(stack[0])
            stack.remove(stack[0])

        return acc

    #build list of result strings
    results = []
    for input in input_stack:
        results.append(process_input(input))
    
    return ','.join(results)
