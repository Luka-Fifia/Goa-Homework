def square_sum(numbers):
    sum = 0
    for i in numbers:
        i *= i
        sum += i
    return sum

# print(square_sum([3, 23, 1, 3]))       testing