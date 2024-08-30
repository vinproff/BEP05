import sys

class RestaurantReservationSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None
        self.menu = {
            "1": {
                "name": "Book a table",
                "options": {
                    "1": {"name": "Small table", "price": 20},
                    "2": {"name": "Medium table", "price": 30},
                    "3": {"name": "Large table", "price": 40},
                    "4": {"name":"extra large table", "price": 50}
                }
            },
            "2": {
                "name": "Preorder food",
                "options": {
                    "1": {"name": "Jollof rice with chicken", "price": 15},
                    "2": {"name": "Fried rice with chicken", "price": 18},
                    "3": {"name": "pounded yam and egusi soup", "price": 25},
                    "4": {"name": "Suya", "price": 10}
                }
            },
            "3": {
                "name": "Preorder drink",
                "options": {
                    "1": {"name": "Non alcoholic drink", "price": 5},
                    "2": {"name": "Wine", "price": 10},
                    "3": {"name": "Malt", "price": 3},
                    "4": {"name": "Mineral", "price": 2}
                }
            },
            "4": {
                "name": "Book a hall",
                "options": {
                    "1": {"name": "Small hall", "price": 100},
                    "2": {"name": "Medium hall", "price": 200},
                    "3": {"name": "Large hall", "price": 300},
                    "4": {"name": "Extra large hall", "price": 400}
                }
            },
            "5": {
                "name": "Book a suite",
                "options": {
                    "1": {"name": "Small suite", "price": 50},
                    "2": {"name": "Medium suite", "price": 100}
                }
            },
        }
        self.orders = []

    def signup(self):
        first_name = input(str("Enter your first name: "))
        last_name = input(str("Enter your last name: "))
        phone = input("Enter your phone number: ")
        email = input("Enter your email: ")
        if '@' and '.' not in email:
            print("please enter a valid email address")
            return
        username = input("Create a username: ")

        if username in self.users:
            print("Username already exists. Try logging in.")
            return

        password = input("Create a password: ")
        self.users[username] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "password": password
        }
        print("Sign-up successful! Please log in.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.users and self.users[username]["password"] == password:
            self.logged_in_user = username
            print(f"Welcome, {self.users[username]['first_name']}!")
            self.show_menu()
        else:
            print("Invalid username or password.")

    def show_menu(self):
        while True:
            print("\nMenu:")
            print("1. Book a table")
            print("2. Preorder food")
            print("3. Preorder drink")
            print("4. Book a hall")
            print("5. Book a suite")
            print("6. Show order")
            print("7. Rate your experience")
            print("8. Logout")
            choice = input("Select an option: ")

            if choice in self.menu:
                self.display_options(choice)
            elif choice == "6":
                self.show_order()
            elif choice == "7":
                self.rate_experience()
            elif choice == "8":
                self.logout()
                break
            else:
                print("Invalid choice. Please try again.")

    def display_options(self, choice):
        options = self.menu[choice]["options"]
        print(f"\n{self.menu[choice]['name']} Options:")
        for opt, details in options.items():
            print(f"{opt}. {details['name']} - ${details['price']}")
        sub_choice = input("Select an option: ")

        if sub_choice in options:
            self.take_order(options[sub_choice])
        else:
            print("Invalid choice. Returning to main menu.")

    def take_order(self, item):
        self.orders.append(item)
        print(f"{item['name']} added to your order.")

    def show_order(self):
        if not self.orders:
            print("Your order is empty.")
            return

        total = 0
        print("\nYour Order:")
        for item in self.orders:
            print(f"{item['name']} - ${item['price']}")
            total += item["price"]
        print(f"Total: ${total}")
        self.payment_options(total)

    def payment_options(self, total):
        print("\nPayment Options:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. Mobile transfer")
        print("4. POS")
        choice = input("Choose your payment method: ")

        if choice in ["1", "2", "3", "4"]:
            print(f"Payment of ${total} successful!")
        else:
            print("Invalid payment option. Please try again.")

    def rate_experience(self):
        print("1. Excellent")
        print("2. Good")
        print("3. Fair")
        print("4. Poor")
        print("5. Very Poor")
        rating = input("Rate your experience (1-5): ")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            print("Thank you for your feedback!")
        else:
            print("Invalid rating. Please rate between 1 and 5.")

    def logout(self):
        print(f"Goodbye, {self.users[self.logged_in_user]['first_name']}!")
        self.logged_in_user = None
        self.orders = []

def main():
    system = RestaurantReservationSystem()

    while True:
        print("\nWelcome to the BEP05 Restaurant Reservation System!")
        print("1. Sign-up")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            system.signup()
        elif choice == "2":
            system.login()
        elif choice == "3":
            print("Exiting the system.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()