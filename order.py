from Modular.menu import menu


def take_order():
    order = {}

    while True:
        items = list(menu.keys())

        print("\nAvailable items:")

        for i, item in enumerate(items, 1):
            print(f"{i}. {item} - ₱{menu[item]:.2f}")

        try:
            choice = int(input("\nEnter item number: "))

            if choice < 1 or choice > len(items):
                print("Invalid item number.")
                continue

            item = items[choice - 1]

        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

        print(f"{quantity} {item}(s) added to your order.")

        again = input(
            "Do you want to order another item? (yes/no): "
        ).lower()

        if again != "yes":
            break

    return order

