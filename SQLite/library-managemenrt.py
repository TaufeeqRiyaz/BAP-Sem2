# menu driven library management system

import sqlite3

# create a connection to the database
conn = sqlite3.connect('library.db')
curs = conn.cursor()
def main_menu():
    print("1. Add book")
    print("2. Delete book")
    print("3. Update book")
    print("4. Search book")
    print("5. Display all books")
    print("6. Exit")
    choice = int(input("Enter your choice - "))
    if choice == 1:
        add_book()
    elif choice == 2:
        delete_book()
    elif choice == 3:
        update_book()
    elif choice == 4:
        search_book()
    elif choice == 5:
        display_books()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        main_menu()

def add_book():
    book_id = input("Enter book id - ")
    title = input("Enter title - ")
    author = input("Enter author - ")
    price = input("Enter price - ")
    curs.execute(f"INSERT INTO books VALUES ('{book_id}', '{title}', '{author}', {price})")
    conn.commit()
    print("Book added successfully")
    main_menu()

def delete_book():
    book_id = input("Enter book id - ")
    curs.execute(f"DELETE FROM books WHERE book_id = '{book_id}'")
    conn.commit()
    print("Book deleted successfully")
    main_menu()

def update_book():
    book_id = input("Enter book id - ")
    title = input("Enter title - ")
    author = input("Enter author - ")
    price = input("Enter price - ")
    curs.execute(f"UPDATE books SET title = '{title}', author = '{author}', price = {price} WHERE book_id = '{book_id}'")
    conn.commit()
    print("Book updated successfully")
    main_menu()

def search_book():
    book_id = input("Enter book id - ")
    curs.execute(f"SELECT * FROM books WHERE book_id = '{book_id}'")
    row = curs.fetchone()
    if row:
        print(row)
    else:
        print("Book not found")
    main_menu()

def display_books():
    curs.execute("SELECT * FROM books")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    main_menu()


# create a table
curs.execute('''CREATE TABLE IF NOT EXISTS books
                (book_id TEXT, title TEXT, author TEXT, price REAL)''')

# insert data into the table
curs.execute("INSERT INTO books VALUES ('1', 'Python', 'Guido van Rossum', 500)")
curs.execute("INSERT INTO books VALUES ('2', 'Java', 'James Gosling', 600)")
curs.execute("INSERT INTO books VALUES ('3', 'C', 'Dennis Ritchie', 400)")

# commit the changes
conn.commit()

main_menu()

# close the connection
conn.close()

