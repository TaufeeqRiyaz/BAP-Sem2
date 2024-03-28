# In[]
def count_words():
    with open("story.txt", "r") as file:
        data = file.read()
        words = data.split()
        return len(words)
print(count_words())