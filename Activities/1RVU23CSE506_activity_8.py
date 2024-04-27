class Bus:
    def __init__(self, bus_number, capacity, route):
        self.bus_number = bus_number
        self.capacity = capacity
        self.route = route

class Passenger:
    def __init__(self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info

class Ticket:
    ticket_number = 1  # Static variable to generate unique ticket numbers
    
    def __init__(self, bus, passenger):
        self.ticket_number = Ticket.ticket_number
        Ticket.ticket_number += 1
        self.bus = bus
        self.passenger = passenger

class ReservationSystem:
    def __init__(self):
        self.available_buses = []
        self.booked_tickets = []

    def book_ticket(self, bus, passenger):
        if len(self.booked_tickets) < bus.capacity:
            ticket = Ticket(bus, passenger)
            self.booked_tickets.append(ticket)
            print(f"Ticket booked successfully! Ticket number: {ticket.ticket_number}")
        else:
            print("Sorry, the bus is already full.")

    def cancel_ticket(self, ticket_number):
        for ticket in self.booked_tickets:
            if ticket.ticket_number == ticket_number:
                self.booked_tickets.remove(ticket)
                print("Ticket canceled successfully.")
                return
        print("Ticket not found.")

    def display_available_buses(self):
        print("Available Buses:")
        for bus in self.available_buses:
            print(f"Bus Number: {bus.bus_number}, Capacity: {bus.capacity}, Route: {bus.route}")

    def display_booked_tickets(self):
        print("Booked Tickets:")
        for ticket in self.booked_tickets:
            print(f"Ticket Number: {ticket.ticket_number}, Bus Number: {ticket.bus.bus_number}, Passenger: {ticket.passenger.name}")


# Menu-driven program
if __name__ == "__main__":
    reservation_system = ReservationSystem()
    while True:
        print("\n Bus Ticket Reservation System")
        print("1. Book a Ticket")
        print("2. Cancel a Ticket")
        print("3. Display Available Buses")
        print("4. Display Booked Tickets")
        print("5. Exit")
        choice = input("Enter your choice - ")

        if choice == "1":
            bus_number = input("Enter Bus Number - ")
            capacity = int(input("Enter Bus Capacity - "))
            route = input("Enter Bus Route - ")
            passenger_name = input("Enter Passenger Name - ")
            age = int(input("Enter Passenger Age - "))
            contact_info = input("Enter Passenger Contact Info - ")
            bus = Bus(bus_number, capacity, route)
            passenger = Passenger(passenger_name, age, contact_info)
            reservation_system.book_ticket(bus, passenger)
        
        elif choice == "2":
            ticket_number = int(input("Enter Ticket Number to Cancel - "))
            reservation_system.cancel_ticket(ticket_number)
        
        elif choice == "3":
            reservation_system.display_available_buses()
        
        elif choice == "4":
            reservation_system.display_booked_tickets()
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")
