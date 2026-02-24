def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #verification data
    test_me = set(sentence.casefold()) #put each char in a set and remove upper case
    tested = test_me.intersection(alphabet) #remove non-letters

    return len(tested) == 26