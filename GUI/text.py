import tkinter as tk
from tkinter import messagebox

def save():
    with open("sample-text.txt", "w") as f:
        out = TB.get("0.1", tk.END)
        f.write(out)
        messagebox.showinfo("Saved", "File saved successfully")
    

root = tk.Tk()

root.title("Text Editor")

TB = tk.Text(root, height=20, width=50)
TB.pack()
B = tk.Button(root, text="Save", command=save)
B.pack()
root.mainloop()