def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation -\n")

print("1.Addition\n")
print("2.Subtraction\n")
print("3.Multiplication\n")
print("4.Division\n")

choice = input("Enter choice(a/s/m/d) - ")
num1 = float(input("Enter first number - "))
num2 = float(input("Enter second number - "))
if choice == 'a':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == 's':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == 'm':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == 'd':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid Input")
