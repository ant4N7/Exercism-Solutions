BANDS = ['black', 'brown', 'red',         #[0, 1, 2,
         'orange', 'yellow', 'green',     # 3, 4, 5,
         'blue', 'violet', 'grey',        # 6, 7, 8,
         'white']                         # 9]


def label(colors):
    tens, ones, zeros, *_= [BANDS.index(c) for c in colors]
    if ones == 0 and zeros % 3 == 2:
        ones, zeros = [-9*tens, zeros+1]
    prefix = ['', 'kilo', 'mega', 'giga']
    
    return f'{10*tens + ones}{"0" * (zeros % 3)} {prefix[zeros // 3]}ohms'
    