def count_positives_sum_negatives(arr):
    sum_negatives = 0
    count_positives = 0

    if len(arr) == 0:
        return []
    
    for i in arr:
        if i > 0:
            count_positives += 1
        else:
            sum_negatives += i
    return [count_positives, sum_negatives]