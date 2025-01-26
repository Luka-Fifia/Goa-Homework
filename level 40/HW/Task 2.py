def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
        
print(stray([1, 1, 1, 1, 1, 1, 2]))