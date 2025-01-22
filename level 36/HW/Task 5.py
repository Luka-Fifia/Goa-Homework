def solution(text, ending):
    lenght_text = len(text)
    lenght_ending = len(ending)

    last_part = text[lenght_text - lenght_ending:]
    
    return last_part == ending