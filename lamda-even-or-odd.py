num = int(input("Enter a number - "))

check_true = (lambda x: True if x % 2 == 0 else False)(num)

print(f"{num} is {'even' if check_true else 'odd'}")