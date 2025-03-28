def lottery(s):
    res = []
    for i in s:
        if i.isdigit():
            if i not in res:
                res.append(i)
    if res:
        return "".join(res)
    else:
        return "One more run!"