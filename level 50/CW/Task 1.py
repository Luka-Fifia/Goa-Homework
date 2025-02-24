def is_isogram(string):
    return len(string.lower()) == len(set([i for i in string.lower()]))