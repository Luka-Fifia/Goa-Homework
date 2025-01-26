def capitals(word):
    result = []
    num = -1
    for char in word:
        num += 1
        if char.isupper():
            result.append(num)
    return result

print(capitals("BmlCBPQTmpkJEzQCmu"))