from string import ascii_lowercase
KEEP = ascii_lowercase + '0123456789'

def cipher_text(plain_text: str) -> str:
    """Implement the classic method for composing secret messages called a square code."""

    #remove spaces and punctuation
    normalized = ''.join(char for char in plain_text.casefold() if char in KEEP)

    #early return for empty string
    if not normalized: return normalized

    #logic for finding number of columns and number of rows
    square = 0
    while square**2 < len(normalized): square += 1
    c,r = square,square-(square*(square-1)>=len(normalized))    

    #pad the end of the string with spaces
    normalized = normalized.ljust(c*r)

    #build the return string
    chunks = [normalized[i:i+c] for i in range(0,c*r,c)]
    return ' '.join(''.join(chunk[i] for chunk in chunks) for i in range(c))
