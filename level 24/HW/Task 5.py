num_of_words = int(input("How many words do you want: "))

words = []


for i in range(num_of_words):
    word = input("Enter Word ")
    words.append(word)

result = ' '.join(words)
print(result)