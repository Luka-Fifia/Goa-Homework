
string = "bobo, bibi, bubu"
emptystr = " "
result = []

for i in string:
    if i == ", ":
        result.append(emptystr)
    else:
        emptystr += i

result.append(emptystr)
print(result)