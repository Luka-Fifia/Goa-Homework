def filter_list(l): 
    result = []

    for char in l:
        if type(char) == int: 
            result.append(char)

    return result