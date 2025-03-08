def invert(lst):
    res = []
    for i in lst:
        if i < 0:
            res.append(abs(i))
        else: 
            res.append(i - (i * 2))
    return res