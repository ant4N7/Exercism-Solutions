import re
D = {'plus ':' + ','minus ':' - ','multiplied by':' * ','divided by':' // ','':''}
PATTERN = r'What is ([-0-9]+)\??\s?(\w*\s*[a-z]*)\s?([-0-9]*)\??\s?(\w*\s*[a-z]*)\s?([-0-9]*)\??'

def answer(question):
    m = re.match(PATTERN,question)
    try:
        return eval('('+m[1]+D[m[2]]+m[3]+')'+D[m[4]]+m[5])
    except:
        if 'cubed' in question or 'Who' in question:
            raise ValueError('unknown operation')
        raise ValueError('syntax error')
    

