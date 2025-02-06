def sum_of_nth_row(n):
    first_number = n ** 2 - (n - 1)
    total = 0
    
    for i in range(n):
        total += first_number + 2 * i
    
    return total