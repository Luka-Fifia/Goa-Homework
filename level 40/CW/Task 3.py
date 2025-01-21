def friend(x):
    result = []
    for char in x:
        if len(char) == 4:
            result.append(char)
    return result