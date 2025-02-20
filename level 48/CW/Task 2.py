def find_short(s):
    words = s.split()
    
    lengths = []
    for word in words:
        lengths.append(len(word))
    
    shortest = min(lengths)
    
    return shortest