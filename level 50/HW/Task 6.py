def open_or_senior(data):
    result = []
    for i in data:
        age = i[0]
        handicup = i[1]
        if age >= 55 and handicup > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result