def find_anagrams(word, candidates):
    anagrams = []

    for candidate in candidates:
        if candidate.lower() != word.lower() and sorted(candidate.lower()) == sorted(word.lower()):
            anagrams.append(candidate)

    return anagrams
    