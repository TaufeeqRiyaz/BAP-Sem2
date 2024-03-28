# write a function to cound the number of lines from story.txt which is not starting with an alphabet T

# In[]
def count_lines():
    count = 0
    with open("story.txt", "r") as file:
        for line in file:
            if line[0] != "T":
                count += 1
    return count
print(count_lines())