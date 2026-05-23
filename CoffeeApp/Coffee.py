# -*- coding: utf-8 -*-

class CoffeeApp:

    def __init__(self):

        # store menu and sales
        self.menu = {
            "Espresso": 145,
            "Latte": 248,
            "Cappuccino": 281,
            "Americano": 198,
            "Mocha": 329,
            "Matcha": 399
        }

        self.sales = 0

        self.orders = []   # store all orders

        self.reviews = []  # store customer reviews

    # show coffee menu
    def show_menu(self):

        print("\n-- Welcome to the Coffee Shop! --")

        print("\n~. Here is our menu .~")

        for coffee, price in self.menu.items():

            print(f"{coffee}: ₹{price}")

    # take order from user
    def take_order(self):

        self.show_menu()

        choice = input(
            "\nPlease enter the name of the coffee you would like to order: "
        )

        if choice in self.menu:

            price = self.menu[choice]

            print(f"{choice} served! ☕")

            self.sales += price

            self.orders.append((choice, price))

        else:

            print(
                "Sorry, we don't have that coffee. Please choose from the menu."
            )

    # print total receipt
    def print_receipt(self):

        if not self.orders:

            print("\n🧾 No orders placed yet.")

            return

        print("\n========== RECEIPT ==========")

        total = 0

        for coffee, price in self.orders:

            print(f"{coffee} : ₹{price}")

            total += price

        print("-----------------------------")

        print(f"Total Bill : ₹{total}")

        print("=============================")

        print("Thank you for your order! Enjoy your coffee! ☕")

    # check total sales
    def view_sales(self):

        print(f"\nTotal Sales: ₹{self.sales}")

    # add customer review
    def add_review(self):

        print("\nRate our Coffee Shop:")

        print("1. ⭐     = Poor")

        print("2. ⭐⭐    = Nice")

        print("3. ⭐⭐⭐   = Satisfactory")

        print("4. ⭐⭐⭐⭐  = Great")

        print("5. ⭐⭐⭐⭐⭐ = Wonderful")

        print("6. Custom Review")

        option = input("\nEnter your choice (1-6): ")

        if option == "1":

            print("\n⭐ Poor")

            improvement = input(
                "What should we do to improve? "
            )

            self.reviews.append(
                f"⭐ Poor - Suggestion: {improvement}"
            )

        elif option == "2":

            print("\n⭐⭐ Nice")

            print(
                "Hope we can match your satisfaction next time."
            )

            self.reviews.append("⭐⭐ Nice")

        elif option == "3":

            print("\n⭐⭐⭐ Satisfactory")

            print("Thank you for your review.")

            self.reviews.append("⭐⭐⭐ Satisfactory")

        elif option == "4":

            print("\n⭐⭐⭐⭐ Great")

            print(
                "Thank you so much for your review!"
            )

            self.reviews.append("⭐⭐⭐⭐ Great")

        elif option == "5":

            print("\n⭐⭐⭐⭐⭐ Wonderful")

            print(
                "Happy to serve you hope we see you next time."
            )

            self.reviews.append("⭐⭐⭐⭐⭐ Wonderful")

        elif option == "6":

            custom = input(
                "\nWrite your custom review: "
            )

            self.reviews.append(
                f"Custom Review: {custom}"
            )

            print(
                "Thank you for your custom review! ☕"
            )

        else:

            print("Invalid choice. Please try again.")

    # view all reviews
    def view_reviews(self):

        if not self.reviews:

            print("\nNo reviews yet.")

        else:

            print("\n--- Customer Reviews ---")

            for i, review in enumerate(
                self.reviews,
                start=1
            ):

                print(f"{i}. {review}")

    # main menu loop
    def run(self):

        while True:

            print("\n.~.=Coffee Shop Menu=.~.")

            print("1. Show Menu")

            print("2. Take Order")

            print("3. Print Receipt")

            print("4. View Total Sales")

            print("5. Add Review")

            print("6. View Reviews")

            print("7. Exit")

            option = input("Choose an option: ")

            if option == "1":

                self.show_menu()

            elif option == "2":

                self.take_order()

            elif option == "3":

                self.print_receipt()

            elif option == "4":

                self.view_sales()

            elif option == "5":

                self.add_review()

            elif option == "6":

                self.view_reviews()

            elif option == "7":

                print(
                    "Thank you for visiting the Coffee Shop! Have a great day! 😊👋"
                )

                break

            else:

                print(
                    "Invalid option. Please try again."
                )


# start the coffee app
app = CoffeeApp()

app.run()