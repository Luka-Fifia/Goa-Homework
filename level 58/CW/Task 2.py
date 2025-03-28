def longest_word(s):
    arr = s.split()
    res = ""
    for i in arr:
        if len(i) >= len(res):
            res = i
    return res