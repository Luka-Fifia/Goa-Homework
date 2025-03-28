def geometric_sequence_elements(a, r, n):
    num = []
    for i in range(n):
        num.append(str(a * r ** i))
    return ", ".join(num)