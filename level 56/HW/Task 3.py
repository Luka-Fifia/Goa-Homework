def even_numbers(arr,n):
    new_arr = []
    for i in arr:
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr[-n:]