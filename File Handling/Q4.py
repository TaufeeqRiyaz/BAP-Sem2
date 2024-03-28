# In[]
def count_lines():
    count = 0
    with open("story.txt", "r") as file:
        for line in file:
            if line[0] != "the":
                count += 1
    return count
print(count_lines())