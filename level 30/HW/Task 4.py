def find_average(numbers):
    if numbers == 0:
        return []
    
    average = 0

    for i in numbers:
        average += i
    return average / len(numbers)