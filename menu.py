menu = {
    "Burger": 89.00,
    "Cheeseburger": 109.00,
    "Chicken Sandwich": 99.00,
    "French Fries": 59.00,
    "Chicken Nuggets": 79.00,
    "Soft Drink": 45.00,
    "Iced Tea": 49.00,
    "Chocolate Sundae": 69.00
}


def display_menu():
    print("\n========== MENU ==========")

    for item, price in menu.items():
        print(f"{item:<25} ₱{price:.2f}")

    print("==========================\n")

