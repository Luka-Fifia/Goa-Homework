def digitize(n): 
    num_str = str(n) 
    arr = []

    for i in num_str: 
        arr.append(int(i))
        arr.reverse()
    return arr