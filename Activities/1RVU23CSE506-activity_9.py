import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect('bus_tickets.db')
c = conn.cursor()

# Create a table to store ticket information
c.execute('''CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                source TEXT,
                destination TEXT,
                date TEXT,
                time TEXT,
                seat_number INTEGER,
                fare REAL
            )''')
conn.commit()

# Function to handle the submit button click event
def submit_ticket():
    name = name_entry.get()
    source = source_entry.get()
    destination = destination_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    seat_number = int(seat_entry.get())
    fare = float(fare_entry.get())

    # Insert the ticket information into the database
    c.execute('''INSERT INTO tickets (name, source, destination, date, time, seat_number, fare)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, source, destination, date, time, seat_number, fare))
    conn.commit()

    # Clear the input fields
    name_entry.delete(0, tk.END)
    source_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    seat_entry.delete(0, tk.END)
    fare_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Bus Ticket Management App")

# Create and place the input fields and labels
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

source_label = tk.Label(window, text="Source:")
source_label.pack()
source_entry = tk.Entry(window)
source_entry.pack()

destination_label = tk.Label(window, text="Destination:")
destination_label.pack()
destination_entry = tk.Entry(window)
destination_entry.pack()

date_label = tk.Label(window, text="Date:")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

time_label = tk.Label(window, text="Time:")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

seat_label = tk.Label(window, text="Seat Number:")
seat_label.pack()
seat_entry = tk.Entry(window)
seat_entry.pack()

fare_label = tk.Label(window, text="Fare:")
fare_label.pack()
fare_entry = tk.Entry(window)
fare_entry.pack()

# Create and place the submit button
submit_button = tk.Button(window, text="Submit", command=submit_ticket)
submit_button.pack()

# Start the main event loop
window.mainloop()

# Close the database connection
conn.close()