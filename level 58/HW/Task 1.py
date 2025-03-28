def vowel_one(s):
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            s = s.replace(i, "1")
        else:
            s = s.replace(i, "0")
    return s