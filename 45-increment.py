nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 46, 47, 48, 49, 50]
new_nums = [i+1 if i > 45 else i for i in nums]
print(new_nums)