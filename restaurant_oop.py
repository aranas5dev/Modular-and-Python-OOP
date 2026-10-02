class Restaurant:

    def __init__(self):
        self.menu = {
            "Burger": 89.00,
            "Cheeseburger": 109.00,
            "Chicken Sandwich": 99.00,
            "French Fries": 59.00,
            "Chicken Nuggets": 79.00,
            "Soft Drink": 45.00,
            "Iced Tea": 49.00,
            "Chocolate Sundae": 69.00
        }

        self.order = {}


    def display_menu(self):
        print("\n========== MENU ==========")

        for item, price in self.menu.items():
            print(f"{item:<25} ₱{price:.2f}")

        print("==========================\n")


    def take_order(self):

        while True:

            items = list(self.menu.keys())

            print("\nAvailable items:")

            for i, item in enumerate(items, 1):
                print(f"{i}. {item} - ₱{self.menu[item]:.2f}")

            # Get item number
            try:
                choice = int(input("\nEnter item number: "))

                if choice < 1 or choice > len(items):
                    print("Invalid item number.")
                    continue

                item = items[choice - 1]

            except ValueError:
                print("Please enter a valid number.")
                continue

            # Get quantity
            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

            except ValueError:
                print("Please enter a valid quantity.")
                continue

            # Add item
            if item in self.order:
                self.order[item] += quantity
            else:
                self.order[item] = quantity

            print(f"{quantity} {item}(s) added to your order.")

            # Continue ordering?
            again = input(
                "Do you want to order another item? (yes/no): "
            ).lower()

            if again != "yes":
                break


    def calculate_total(self):

        total = 0

        for item, quantity in self.order.items():
            total += self.menu[item] * quantity

        return total


    def print_receipt(self):

        print("\n==============================================")
        print("             RESTAURANT RECEIPT")
        print("==============================================")

        for item, quantity in self.order.items():

            price = self.menu[item]
            item_total = price * quantity

            print(
                f"{item:<22} "
                f"{quantity:>3} x "
                f"₱{price:>7.2f} = "
                f"₱{item_total:>8.2f}"
            )

        total = self.calculate_total()

        print("----------------------------------------------")
        print(f"{'TOTAL':<35} ₱{total:.2f}")
        print("==============================================")
        print("       Thank you for your order!")
        print("==============================================")


    def run(self):

        self.display_menu()

        answer = input("Do you want to order? (yes/no): ").lower()

        if answer == "yes":

            self.take_order()

            if len(self.order) > 0:
                self.print_receipt()
            else:
                print("No items were ordered.")

        else:
            print("Thank you! Have a nice day.")


# Create object
restaurant = Restaurant()

# Run program
restaurant.run()

