def sequence_sum(a, b, c):
    res = 0
    for i in range(a, b + 1, c):
        res += i
    return res