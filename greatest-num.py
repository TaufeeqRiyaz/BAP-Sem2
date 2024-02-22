# use lamda function to find greatest of two numbers

num_1 = int(input("Enter a number - "))
num_2 = int(input("Enter another number - "))

greatest = lambda x, y: x if x > y else y (num_1, num_2)
print(greatest)