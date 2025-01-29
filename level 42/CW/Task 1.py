def points(games):
    points = 0
    
    for i in games:
        x = int(i[0])
        y = int(i[2])
        
        if x > y:
            points += 3
        elif x == y:
            points += 1
            
    return points