def count_arara(n):
    two = "adak"
    one = "anane"
    res = []
    for i in range(n // 2):
        res.append(two)
    if n % 2 == 1:
        res.append(one)        
    return " ".join(res)