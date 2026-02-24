BANDS = ['black', 'brown', 'red', 
         'orange', 'yellow', 'green',
         'blue', 'violet', 'grey',
         'white']


def label(colors):
    tens, ones, zeros, *_= [BANDS.index(c) for c in colors]
    if ones == 0 and zeros % 3 == 2:
        ones, zeros = [-9*tens, zeros+1]
    prefix = ['', 'kilo', 'mega', 'giga']
    
    return f'{10*tens + ones}{"0" * (zeros % 3)} {prefix[zeros // 3]}ohms'
    