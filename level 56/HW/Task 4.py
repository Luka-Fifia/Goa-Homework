def vowel_indices(word):
    vowels = "aeiouyAIEOUY"
    res = []
    for char in range(len(word)):
        if word[char] in vowels:
            res.append(char+1)
    return res