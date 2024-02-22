num1 = int(input("Enter the number of elements in the array - "))

arr = []

for i in range(num1):
    arr.append(int(input("Enter the element - ")))

print(sum(arr))