def descending_order(num):
    arr = []
    for i in str(num):
        arr.append(i)
    arr.sort()
    arr.reverse()
    return int(''.join(arr))