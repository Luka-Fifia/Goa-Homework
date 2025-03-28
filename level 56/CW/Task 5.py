def solve(s):
    lower = 0
    upper = 0
    for i in s:
        if i.islower():
            lower += 1
        else:
            upper += 1
    if lower >= upper:
        return s.lower()
    return s.upper()