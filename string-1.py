num_of_names = int(input("Enter the number of names - "))
names = []

for i in range(num_of_names):
    names.append(input("Enter the name - "))

print("The names are - ", names)

for name in names:
    print(name, name.count("a") + name.count("A"))