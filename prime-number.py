def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

num = int(input("Enter a number - "))
if prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")