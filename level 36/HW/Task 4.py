def find_short(s): 
    words = s.split() 
    shortest_word_lenght = []

    for i in words:
        char = len(i)
        shortest_word_lenght.append(char)
        
    return min(shortest_word_lenght)