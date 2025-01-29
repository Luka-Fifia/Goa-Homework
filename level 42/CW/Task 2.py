def to_binary(n):
    arr = []
    while n > 0:
        binary =n % 2
        arr.append(str(binary))
        n //= 2
    return ''.join(arr[::-1])

print(to_binary(16))