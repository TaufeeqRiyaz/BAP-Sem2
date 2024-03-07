# In[1]:
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

# In[2]:

c = a + b
print(f"The sum of tuple A and B is {c}")

# In[3]:

d = sorted(c)
print(f"The sorted copy of tuple C is {d}")
print(f"The third element of tuple D is {d[2]}")

# In[4]:
print(f"The last 3 elements of tuple D are {d[-3:]}")
print(f"The length of tuple D is {len(d)}")

# In[5]:
 #read marks of n students in a course as a tuple and find the sum average and higest and lowest
n = int(input("Enter the number of students - "))
marks = []
for i in range(n):
    marks.append(float(input(f"Enter marks of student {i+1} - "))
)
marks = tuple(marks)
print(f"The sum of marks of students is {sum(marks)}")
print(f"The average of marks of students is {sum(marks)/n}")
print(f"The highest marks of students is {max(marks)}")
print(f"The lowest marks of students is {min(marks)}")
