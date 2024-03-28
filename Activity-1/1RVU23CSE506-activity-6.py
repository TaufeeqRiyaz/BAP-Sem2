# In[]
# Level - 1

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# 1. Plot a pair plot for numerical features
sns.pairplot(titanic.select_dtypes(include=['float64', 'int64']))
plt.show()

# 2. Create a bar graph to show the count of passengers in each class
sns.countplot(x='class', data=titanic)
plt.show()

# 3. Generate a violin plot to visualize the distribution of age by passenger class
sns.violinplot(x='class', y='age', data=titanic)
plt.show()

# 4. Plot a scatter plot between age and fare
sns.scatterplot(x='age', y='fare', data=titanic)
plt.show()

# 5. Create a bar graph to show the count of passengers by embarked location
sns.countplot(x='embarked', data=titanic)
plt.show()

# 6. Plot a heatmap to visualize the correlation matrix of numerical features
numerical_columns = titanic.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = titanic[numerical_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# 7. Create a swarm plot to compare age distributions by passenger class
sns.swarmplot(x='class', y='age', data=titanic)
plt.show()

# 8. Generate a histogram for age
sns.histplot(titanic['age'].dropna(), kde=False, bins=30)
plt.show()

# 9. Plot a line plot to show the trend of fare amounts over the index
plt.plot(titanic.index, titanic['fare'])
plt.xlabel('Index')
plt.ylabel('Fare')
plt.title('Trend of Fare Amounts')
plt.show()

# 10. Create a bar graph to show the average fare for each class
sns.barplot(x='class', y='fare', data=titanic, estimator=lambda x: sum(x) / len(x))
plt.show()



#In[]
# Level - 2
def add_student(admission_number, name, percentage):
    with open("STUDENT.TXT", "a") as file:
        file.write(f"{admission_number}, {name}, {percentage}\n")

def delete_student(admission_number):
    with open("STUDENT.TXT", "r") as file:
        lines = file.readlines()
    with open("STUDENT.TXT", "w") as file:
        for line in lines:
            if line.split(",")[0] != admission_number:
                file.write(line)

def update_student(admission_number, name, percentage):
    with open("STUDENT.TXT", "r") as file:
        lines = file.readlines()
    with open("STUDENT.TXT", "w") as file:
        for line in lines:
            if line.split(",")[0] == admission_number:
                file.write(f"{admission_number}, {name}, {percentage}\n")
            else:
                file.write(line)

def search_student(admission_number):
    with open("STUDENT.TXT", "r") as file:
        for line in file:
            if line.split(",")[0] == admission_number:
                return line
    return None

def count_rec():
    count = 0
    with open("STUDENT.TXT", "r") as file:
        for line in file:
            if float(line.split(",")[2]) > 75:
                count += 1
                print(line)
    return count

# menu driven program
while True:
    print("1. Add student")
    print("2. Delete student")
    print("3. Update student")
    print("4. Search student")
    print("5. Display students with percentage above 75")
    print("6. Exit")
    choice = int(input("Enter your choice - "))
    if choice == 1:
        admission_number = input("Enter admission number - ")
        name = input("Enter name - ")
        percentage = input("Enter percentage - ")
        add_student(admission_number, name, percentage)
    elif choice == 2:
        admission_number = input("Enter admission number - ")
        delete_student(admission_number)
    elif choice == 3:
        admission_number = input("Enter admission number - ")
        name = input("Enter name - ")
        percentage = input("Enter percentage - ")
        update_student(admission_number, name, percentage)
    elif choice == 4:
        admission_number = input("Enter admission number - ")
        student = search_student(admission_number)
        if student:
            print(student)
        else:
            print("Student not found")
    elif choice == 5:
        print(count_rec())
    elif choice == 6:
        break
    else:
        print("Invalid choice")