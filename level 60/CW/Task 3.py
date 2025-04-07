def max_possible_score(questions, new):
    new_set = set(new)
    total_score = 0
    
    for i in questions:
        points = questions[i] 
        if i in new_set:
            total_score += points * 2
        else:
            total_score += points
    return total_score