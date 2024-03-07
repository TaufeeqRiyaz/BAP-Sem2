num = int(input("Enter the number of words - "))

words = []

for i in range(num):
    word = input("Enter the word - ")
    words.append(word)

last_letters = [word[-1] for word in words]

print(last_letters)