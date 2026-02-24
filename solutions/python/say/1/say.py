ZERO_TO_19 = ['zero','one','two','three','four','five','six','seven','eight',
              'nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
              'sixteen','seventeen','eighteen','nineteen']
TENS = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
SCALE = ['',' thousand',' million',' billion',' trillion']

def _say99(number):
    if not number: return ''
    if 0<number<20:
        return ZERO_TO_19[number]
    number = str(number)
    if number[-1] == '0':
        return TENS[int(number[0])-2]
    return TENS[int(number[0])-2]+'-'+ZERO_TO_19[int(number[1])]
    
def _say999(number):
    number = str(number)
    if number[-2:] == '00':
        return ZERO_TO_19[int(number[0])] + ' hundred'
    return ZERO_TO_19[int(number[0])] + ' hundred ' + _say99(int(number[1:]))

def say(number: int) -> str:
    if not 0<=number<1e12:
        raise ValueError("input out of range")
    if not number: return 'zero'
    if number < 100: return _say99(number)
    if number < 1000: return _say999(number)        

    thousands = []
    for _ in range(len(str(number))//3+1):
        thousands.append(number%1000)
        number //= 1000

    result = []
    for digits in thousands:
        if digits < 100:
            result.append(_say99(digits))
        else: result.append(_say999(digits))
    for i,r in enumerate(result):
        if r: result[i] += SCALE[i]

    print(result)
    return ' '.join(s for s in result[::-1] if s)
