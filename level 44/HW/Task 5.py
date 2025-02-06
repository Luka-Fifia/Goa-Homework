def divisors(n):
    result = []
    for i in range(2, n):
        if n % i == 0:
            result.append(i)
    
    if result:
        return result
    else:
        return f"{n} is prime"