def printer_error(s):
    eror_count = 0
    for i in s:
        if i > "m":
            eror_count += 1
    lenght = len(s)
    return str(eror_count) + "/" + str(lenght)