def AddToDatabase(name, surname, age):
    dictionary = {
        "name" : "",
        "surname" : "",
        "age" : 0
    }
    dictionary["name"] = name
    dictionary["surname"] = surname
    dictionary["age"] = age

    return dictionary

print(AddToDatabase("luka", "Gela", 14))