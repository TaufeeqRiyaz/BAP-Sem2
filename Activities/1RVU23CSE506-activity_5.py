#In[1]
# [Level-1 question 1 soluion]
def count_letters(s):
    s = s.replace(" ", "")
    s = s.lower()
    letter_count = {}
    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

#In[2]
# Level-1 question 2 soluion
def generate_dict():
    d = {}
    for i in range(1, 21):
        d[i] = i**2
    return d

#In[3]
#In [Level-2 question 3 soluion]
def total_amount_paid(items):
    price_list = {
        "Biscuit": 10,
        "BREAD": 20,
        "SUGAR": 84,
        "JAM": 40,
        "CHEESE": 130,
        "BOURNVITA": 240,
        "TEA Powder": 200,
        "MILK": 30,
        "COFFEE Powder": 40,
        "CORNFLAKES": 56,
        "RICE": 78,
        "DAL": 100
    }
    total = 0
    for item in items:
        total += price_list[item]
    return total

elango_items = [
    "SUGAR", "JAM", "CHEESE", "BOURNVITA", "TEA Powder", "CORNFLAKES", "CHEESE", "BOURNVITA",
    "TEA Powder", "CORNFLAKES", "Biscuit", "BREAD", "SUGAR", "JAM", "CHEESE", "BOURNVITA",
    "TEA Powder", "MILK", "COFFEE Powder", "CORNFLAKES", "RICE", "DAL"
]
raja_items = [
    "SUGAR", "JAM", "CHEESE", "BOURNVITA", "TEA Powder", "CORNFLAKES", "CHEESE", "BOURNVITA",
    "CHEESE", "BOURNVITA", "TEA Powder", "MILK"
]

elango_total = total_amount_paid(elango_items)
raja_total = total_amount_paid(raja_items)

print("Total amount paid by Elango -", elango_total)
print("Total amount paid by Raja -", raja_total)