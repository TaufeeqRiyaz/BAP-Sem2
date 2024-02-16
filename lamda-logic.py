num = int(input("Enter a number - "))

# if value < 10 then return by multiplying by 2
# if 10 < value < 20 then return by multiplying 3
# else return original value

new_value = (lambda x: x*2 if x < 10 else (x*3 if 10 < x < 20 else x))(num)
print(new_value)