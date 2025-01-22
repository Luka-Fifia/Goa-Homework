def get_middle(s): 
    lenght = len(s) 
    mid = lenght // 2

    if lenght % 2 == 0:
        return s[mid - 1] + s[mid]
    else:
        return s[mid]