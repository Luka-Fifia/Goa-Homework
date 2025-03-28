def count_letters_and_digits(s):
    res = 0
    for i in s:
        if i.isalnum():
            res += 1
    return res