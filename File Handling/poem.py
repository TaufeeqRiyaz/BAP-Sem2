#In[]
def poem():
    with open("poem.txt", "r") as file:
        for line in file:
            print(line, end="")
poem()