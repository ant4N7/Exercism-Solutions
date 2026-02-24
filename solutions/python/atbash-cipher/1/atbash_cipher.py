from string import ascii_lowercase,punctuation

CIPHER = str.maketrans(ascii_lowercase, ascii_lowercase[::-1],punctuation+' ')

def encode(plain_text):
    raw_cipher = plain_text.casefold().translate(CIPHER)
    return ' '.join(raw_cipher[i:i+5] for i in range(0,len(raw_cipher),5))


def decode(ciphered_text):
    return ciphered_text.translate(CIPHER)
