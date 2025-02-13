def high_and_low(numbers):
    numbers = numbers.split()
    list = []
    
    for i in numbers:
        list.append(int(i))
    
    min_num = min(list)
    max_num = max(list)
    
    return f"{max_num} {min_num}"