
num_1 = int(input("Enter a number - "))
num_2 = int(input("Enter another number - "))

gcd = lambda a, b: a if b == 0 else gcd(b, a % b) (num_1, num_2)

print(gcd)