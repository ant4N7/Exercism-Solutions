import re

def decode(string: str) -> str:
    pattern = r'(\d+)(\D)'  #this regex captures one or more digits in group(1)
                            #then captures a single non-digit in group(2)

    return re.sub(pattern,lambda m: m.group(2)*int(m.group(1)),string)


def encode(string: str) -> str:
    pattern = r'(\D)\1+'    #this regex captures a single non digit in group(1)
                            #the \1 is a backreference to group(1) and the + means 1 or more times
                            #group(0) is the entire pattern matched by the regex

    return re.sub(pattern,lambda m: f'{len(m.group(0))}{m.group(1)}',string)
