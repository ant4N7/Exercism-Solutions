TOLERANCE_BAND_DICT = {'grey': '±0.05%', 'violet': '±0.1%', 'blue': '±0.25%', 'green': '±0.5%', 'brown': '±1%', 'red': '±2%', 'gold': '±5%', 'silver': '±10%'}
RESISTANCE_BAND_LIST = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
PREFIX = ['', 'kilo', 'mega', 'giga']

def resistor_label(colors):
    
    #'0 ohms' for 1 band
    if len(colors) == 1:
        return '0 ohms'

    #unpack strings from colors list and set variables
    *res_bands, zeros, tol_band = colors
    res_bands = ''.join(str(digit) for digit in [RESISTANCE_BAND_LIST.index(band) for band in res_bands])
    zeros = RESISTANCE_BAND_LIST.index((zeros))
    tolerance = TOLERANCE_BAND_DICT[tol_band]
    

    #calculate resistance
    resistance = int(res_bands + '0' * zeros)

    #determine prefix
    index = 0
    while resistance % 1000 == 0:
        resistance //= 1000
        index += 1

    #build return string
    if len(str(resistance)) > 3:
        return f'{resistance/1000} {PREFIX[index+1]}ohms {tolerance}'
    return f'{resistance} {PREFIX[index]}ohms {tolerance}'
