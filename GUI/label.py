import tkinter as tk

root = tk.Tk()
root.title("First Tinkter GUI")

root.geometry("1900x1080")

label = tk.Label(root, text="Hello World!" , font=('Arial', 24))
label.pack()

root.mainloop()