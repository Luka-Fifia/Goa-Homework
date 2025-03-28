def series_sum(n):
    if n == 0:
        return "0.00" 
    res = 0
    for i in range(n):
        res += 1 / (1 + 3 * i)    
    return f"{res:.2f}"