def rotate(text, key):
    cipher = ''
    for c in text:
        if 97 <= ord(c) <= 122:
            cipher += chr(ord(c) + key) if ord(c) + key <= 122 else chr(ord(c) + (key-26))
        elif 65 <= ord(c) <= 90:
            cipher += chr(ord(c) + key) if ord(c) + key <= 90 else chr(ord(c) + (key-26))
        else:
            cipher +=c
    return cipher
