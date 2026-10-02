from menu import menu


def calculate_total(order):
    total = 0

    for item, quantity in order.items():
        total += menu[item] * quantity

    return total


def print_receipt(order):
    print("\n==============================================")
    print("             RESTAURANT RECEIPT")
    print("==============================================")

    for item, quantity in order.items():
        price = menu[item]
        item_total = price * quantity

        print(
            f"{item:<22} "
            f"{quantity:>3} x "
            f"₱{price:>7.2f} = "
            f"₱{item_total:>8.2f}"
        )

    total = calculate_total(order)

    print("----------------------------------------------")
    print(f"{'TOTAL':<35} ₱{total:.2f}")
    print("==============================================")
    print("       Thank you for your order!")
    print("==============================================")