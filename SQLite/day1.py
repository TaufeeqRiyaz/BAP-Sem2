# intro to sqlite

import sqlite3

# create a connection to the database
conn = sqlite3.connect('example.db')
curs = conn.cursor()

# create a table

curs.execute('''CREATE TABLE IF NOT EXISTS students
                (usn TEXT, name TEXT, age INTEGER)''')

# insert data into the table
curs.execute("INSERT INTO students VALUES ('1RVU23CSE506', 'Taufeeq', 19)")
curs.execute("INSERT INTO students VALUES ('1RVU23CSE507', 'Rahul', 20)")
curs.execute("INSERT INTO students VALUES ('1RVU23CSE508', 'Raj', 21)")
curs.execute("INSERT INTO students VALUES ('1RVU23CSE509', 'Ravi', 22)")
curs.execute("INSERT INTO students VALUES ('1RV23CSE510' , 'Harsha', 23)")

# commit the changes
conn.commit()

# select data from the table
curs.execute("SELECT * FROM students")
rows = curs.fetchall()
for row in rows:
    print(row)

# close the connection
conn.close()
