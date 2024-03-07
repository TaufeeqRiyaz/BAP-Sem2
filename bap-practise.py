# In[1]:

rows = int(input("Enter the number of rows - "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# In[2]:
rows = int(input("Enter the number of rows - "))
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(" ", end="")
    k=1
    while k<=2*i-1:
        print("*", end="")
        k+=1
    print()
# %%
