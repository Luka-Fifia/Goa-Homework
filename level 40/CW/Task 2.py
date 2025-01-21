def is_isogram(st):   
    a = set()  
    for char in st.lower():
        a.add(char)
    if len(st) == len(a):
        print(True)
    else:
        print(False)

# print(is_isogram("weassd"))           testing