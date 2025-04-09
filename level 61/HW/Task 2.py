def to_alternating_case(s):
    res = ""
    for i in range(len(s)):
        if s[i].islower():
            res += s[i].upper()
        else:
            res += s[i].lower()
    return res