import tkinter as tk

root = tk.Tk()
root.title("Library Management System")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    print(title, author, year)

def delete_book():
    book_id = delete_entry.get()
    print(book_id) 

add_frame = tk.LabelFrame(root, text="Add Book", padx=10, pady=10)
add_frame.grid(row=0, column=0, padx=10, pady=10)

title_label = tk.Label(add_frame, text="Title")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(add_frame)
title_entry.grid(row=0, column=1)

author_label = tk.Label(add_frame, text="Author")
author_label.grid(row=1, column=0)
author_entry = tk.Entry(add_frame)
author_entry.grid(row=1, column=1)

year_label = tk.Label(add_frame, text="Year")
year_label.grid(row=2, column=0)
year_entry = tk.Entry(add_frame)
year_entry.grid(row=2, column=1)

add_button = tk.Button(add_frame, text="Add Book", command=add_book)
add_button.grid(row=3, column=0, columnspan=2)

delete_frame = tk.LabelFrame(root, text="Delete Book", padx=10, pady=10)
delete_frame.grid(row=0, column=1, padx=10, pady=10)

delete_label = tk.Label(delete_frame, text="Book ID")
delete_label.grid(row=0, column=0)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=1)

delete_button = tk.Button(delete_frame, text="Delete Book", command=delete_book)
delete_button.grid(row=1, column=0, columnspan=2)

