# question 6.1

age = int(input("Enter your age - "))
health = input("Enter your health status (excellent/poor) - ").lower()
location = input("Enter your location (city/village) - ").lower()
gender = input("Enter your gender (male/female) - ").lower()

if 25 <= age <= 35:
    if health == "excellent":
        if location == "city" and gender == "male":
            premium = 4000
            max_policy_amount = 200000
            print(f"You are Insured! \nPremium - Rs. {premium} \nMax Policy Amount - Rs. {max_policy_amount}")
        elif location == "city" and gender == "female":
            premium = 3000
            max_policy_amount = 100000
            print(f"You are Insured! \nPremium - Rs. {premium} \nMax Policy Amount - Rs. {max_policy_amount}")
        elif location == "village" and gender == "male":
            premium = 6000
            max_policy_amount = 50000
            print(f"You are Insured! \nPremium - Rs. {premium} \nMax Policy Amount - Rs. {max_policy_amount}")
        else:
            print("You are Not insured")
    else:
        print("Your are Not insured")
else:
    print("You are Not insured")


# question 6.2

sales_amount = float(input("Enter total sales amount - "))

if sales_amount >= 100000:
    basic = 5000
    hra_percentage = 20
    da_percentage = 110
    conveyance = 500
    incentive_percentage = 10
    bonus = 1000
else:
    basic = 4000
    hra_percentage = 10
    da_percentage = 110
    conveyance = 500
    incentive_percentage = 5
    bonus = 500

hra = (hra_percentage / 100) * basic
da = (da_percentage / 100) * basic
incentive = (incentive_percentage / 100) * sales_amount

gross_salary = basic + hra + da + conveyance + incentive + bonus

print(f"Gross Salary is Rs. {gross_salary}")
