text = "xinkali cudia"
old = "cudia"
new = "sauketesoa"

result = ""
i = 0
while i < len(text):
    if text[i:i+len(old)] == old:
        result += new
        i += len(old)
    else:
        result += text[i]
        i += 1

print(result)