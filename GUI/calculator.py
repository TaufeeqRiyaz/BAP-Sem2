import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Error: Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Styling
root.geometry("300x200")
root.resizable(False, False)
root.configure(background='#f0f0f0')

# Input boxes
entry1 = tk.Entry(root, width=10, font=('Arial', 12))
entry1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

entry2 = tk.Entry(root, width=10, font=('Arial', 12))
entry2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Dropdown menu for operation selection
operation_var = tk.StringVar(root)
operations = ['+', '-', '*', '/']
operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=operations, font=('Arial', 12), width=5)
operation_dropdown.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
operation_dropdown.current(0)

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 12), bg='#4CAF50', fg='#ffffff')
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

# Label to display result
result_label = tk.Label(root, text="Result: ", font=('Arial', 12), bg='#f0f0f0')
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

# Centering the window
root.eval('tk::PlaceWindow . center')

root.mainloop()
