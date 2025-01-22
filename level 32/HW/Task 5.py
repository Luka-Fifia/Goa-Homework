def high_and_low(numbers): 
    num_arr = numbers.split() 
    num_list = []
    
    for i in num_arr:
        num_list.append(int(i))

    highest = max(num_list)
    lowest = min(num_list)

    return f" {highest} {lowest}"