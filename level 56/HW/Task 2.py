def even_or_odd(s):
    sum_even = 0
    sum_odd = 0
    for i in s:
        if int(i) % 2 == 0:
            sum_even += int(i)
        else:
            sum_odd += int(i)
    if sum_odd < sum_even:
        return "Even is greater than Odd"
    elif sum_odd > sum_even:
        return "Odd is greater than Even"
    return "Even and Odd are the same"