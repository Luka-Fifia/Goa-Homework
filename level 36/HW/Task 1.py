def filter_list(l): 
    arr = [] 
    for i in l:
        if type(i) != str: 
            arr.append(i)
    return arr