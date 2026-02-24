TOLERANCE_BAND_DICT = {'grey': '±0.05%', 'violet': '±0.1%', 'blue': '±0.25%', 'green': '±0.5%', 'brown': '±1%', 'red': '±2%', 'gold': '±5%', 'silver': '±10%'}
RESISTANCE_BAND_LIST = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
PREFIX = ['', 'kilo', 'mega', 'giga']

def resistor_label(colors):
    
    #'0 ohms' for 1 band
    if len(colors) == 1:
        return '0 ohms'

    #extract variables from colors list
    *res_bands, zeros, tol_band = colors

    #calculate resistance
    resistance = int(''.join(str(i) for i in [RESISTANCE_BAND_LIST.index(b) for b in res_bands]) + ('0' * (RESISTANCE_BAND_LIST.index(zeros))))

    #determine prefix
    z = 0
    while resistance % 1000 == 0:
        resistance //= 1000
        z += 1

    #build return string
    if len(str(resistance)) > 3:
        return f'{resistance/1000} {PREFIX[z+1]}ohms {TOLERANCE_BAND_DICT[tol_band]}'
    return f'{resistance} {PREFIX[z]}ohms {TOLERANCE_BAND_DICT[tol_band]}'
