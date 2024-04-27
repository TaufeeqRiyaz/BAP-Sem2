# question 6.1

def classify_bmi(bmi_list):

    underweight_bmi = []
    normal_bmi = []
    overweight_bmi = []

    for bmi in bmi_list:
        if 0 <= bmi < 18.5:
            underweight_bmi.append(bmi)
        elif 18.5 <= bmi < 25:
            normal_bmi.append(bmi)
        elif bmi >= 25:
            overweight_bmi.append(bmi)
        else:
            print(f"Invalid BMI value: {bmi}. Please enter a value between 0 and 50.")

    return underweight_bmi, normal_bmi, overweight_bmi


n = int(input("Enter the number of people - "))
bmi_list = []
for i in range(n):
    try:
        bmi = float(input(f"Enter BMI value for person {i+1} - "))
        bmi_list.append(bmi)
    except ValueError:
        print("Invalid input. Please enter a numerical BMI value.")
underweight_bmi, normal_bmi, overweight_bmi = classify_bmi(bmi_list)
print("\nBMI Categories -")
print("- Underweight -", underweight_bmi)
print("- Normal Range -", normal_bmi)
print("- Overweight -", overweight_bmi)



# question 6.2

movies = []

reservations = []

def add_movie():
    title = input("Enter movie title - ")
    showtimes = input("Enter showtimes (comma-separated) - ").split(", ")
    available_seats = input("Enter available seats (comma-separated) - ").split(", ")
    movie = {"title": title, "showtimes": showtimes, "available_seats": available_seats}
    movies.append(movie)
    print("Movie added successfully!")

def reserve_ticket():
    customer_name = input("Enter customer name - ")
    movie_title = input("Enter movie title - ")
    showtime = input("Enter showtime - ")
    seat = input("Enter seat - ")
    for movie in movies:
        if movie["title"] == movie_title and showtime in movie["showtimes"] and seat in movie["available_seats"]:
            movie["available_seats"].remove(seat)
            reservation = {"customer_name": customer_name, "movie_title": movie_title, "showtime": showtime, "seat": seat}
            reservations.append(reservation)
            print("Ticket reserved successfully!")
            return
    print("Sorry, the requested ticket could not be reserved.")

def cancel_reservation():
    customer_name = input("Enter customer name - ")
    for reservation in reservations:
        if reservation["customer_name"] == customer_name:
            for movie in movies:
                if movie["title"] == reservation["movie_title"] and reservation["showtime"] in movie["showtimes"]:
                    movie["available_seats"].append(reservation["seat"])
                    reservations.remove(reservation)
                    print("Reservation canceled successfully!")
                    return
    print("No reservation found for the given customer name.")

add_movie()

reserve_ticket()

cancel_reservation()
