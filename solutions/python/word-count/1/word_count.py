import re

def count_words(sentence: str) -> dict[str, int]:

    list_words = [match[0] for match in re.finditer(r'[a-z0-9]+(\'\w\w?)?',sentence.casefold())]
    res = {}
    for word in list_words:
        res.update({word: list_words.count(word)})
    return res
