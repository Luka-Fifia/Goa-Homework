def xo(s):
    count_x = 0
    count_o = 0
    for i in s:
        if i.lower() == "x":
            count_x += 1
        elif i.lower() == "o":
            count_o += 1
    return count_x == count_o

def xo(s):
    return s.lower().count("x") == s.lower().count("o")