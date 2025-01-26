def remove_duplicates(s):   

    result = []
    for char in s.split():
        if char not in result:
            result.append(char)

    return " ".join(result)
