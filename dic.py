
#In[1]

temps = [68.8, 70.2, 67.2, 71.8, 73.2, 75.6, 74.0]
days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
temp_dict = {day: temp for day, temp in zip(days, temps)}
print(temp_dict)
day = input("Enter the day - ")
print(f"The average temperature on {day} is {temp_dict[day]} F")



# %%
n = int(input("Enter a number - "))
squares = {i: i*i for i in range(1, n+1)}
print(squares)
# %%

# return a list that prince tem btw 70 to 79 from temps
temps = [68.8, 70.2, 67.2, 71.8, 73.2, 75.6, 74.0]

sorted_temp = {day: temp for day, temp in zip(days, temps) if 70 <= temp <= 79}
print(sorted_temp)

# %%
