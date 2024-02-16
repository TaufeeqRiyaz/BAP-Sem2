def prime_number(num, i=2):
    if num < 2:
        return False
    if num == i:
        return True
    if num % i == 0:
        return False
    return prime_number(num, i+1)

num = int(input("Enter a number - "))
if prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

