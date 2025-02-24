def accum(st):
    res = ""
    num = 1
    for i in st:
        res += (i * num)
        num += 1
        res += "-"
    return res.title()[:-1]