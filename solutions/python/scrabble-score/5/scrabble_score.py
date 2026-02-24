def score(w):
    return sum([s if c in l else 0 for s,l in \
                {1:"aeioulnrst",2:"dg",3:"bcmp",4:"fhvwy",5:"k",8:"jx",10:"qz"}.items() \
                for c in w.lower()])
    