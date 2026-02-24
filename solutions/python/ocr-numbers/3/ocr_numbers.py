NUM_DICT = {(' _ ', '| |', '|_|', '   '):'0',('   ', '  |', '  |', '   '):'1',
            (' _ ', ' _|', '|_ ', '   '):'2',(' _ ', ' _|', ' _|', '   '):'3',
            ('   ', '|_|', '  |', '   '):'4',(' _ ', '|_ ', ' _|', '   '):'5',
            (' _ ', '|_ ', '|_|', '   '):'6',(' _ ', '  |', '  |', '   '):'7',
            (' _ ', '|_|', '|_|', '   '):'8',(' _ ', '|_|', ' _|', '   '):'9'}


def convert(input_grid: list[str]) -> str:
    '''converts multiple lines of OCR numbers to a string of digits separated by commas'''
    
    if len(input_grid) % 4:
        raise ValueError('Number of input lines is not a multiple of four')
    if any(len(col) % 3 for col in input_grid):
        raise ValueError('Number of input columns is not a multiple of three')

    # split lines of digits into groups
    input_stack = [input_grid[i:i+4] for i in range(0,len(input_grid),4)]

    # use _process_inputs() to join lines of OCR numbers with commas
    return ','.join(_process_input(OCR_line) for OCR_line in input_stack)


def _process_input(OCR_line: list[str]) -> str:
    '''converts a single line of OCR numbers to a string of digits'''

    # determine the number of digits in the line and initialize result as a string
    num_digits = len(OCR_line[0]) // 3
    result = ""

    # group string slices into NUM_DICT keys and concat items in result
    for i in range(num_digits):
        key = tuple(line[i * 3:(i + 1) * 3] for line in OCR_line)
        result += NUM_DICT.get(key, '?')

    return result
