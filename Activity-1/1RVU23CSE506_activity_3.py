# question 6.1

def count(sentence):
    letters = 0
    digits = 0
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

sentence = input("Enter a sentence - ")
letters, digits = count(sentence)
print("LETTERS", letters)
print("DIGITS", digits)


#question 6.2

def left_rotate(s, d):
    return s[d:] + s[:d]

def right_rotate(s, d):
    return s[-d:] + s[:-d]

s = input("Enter a string - ")
d = int(input("Enter the number - "))
print("Left rotation:", left_rotate(s, d))
print("Right rotation:", right_rotate(s, d))


#question 6.3

def remove_symbols(string):
    cleaned_string = ''.join(char for char in string if char.isalnum())
    return cleaned_string.capitalize()

input_string = input("Enter a string - ")
output_string = remove_symbols(input_string)
print(output_string)
