import tkinter as tk

def button_click():
    user_input = entry.get()
    output_label.config(text=user_input)

root = tk.Tk()
root.title("Entry and Button")

entry = tk.Entry(root, width=20, font=('Arial', 12))
entry.pack(pady=10)

button = tk.Button(root, text="Click Me", command=button_click, font=('Arial', 12))
button.pack(pady=5)

output_label = tk.Label(root, text="", font=('Arial', 12))
output_label.pack(pady=10)
root.mainloop()