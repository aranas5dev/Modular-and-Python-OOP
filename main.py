from menu import display_menu
from order import take_order
from receipt import print_receipt


def main():
    display_menu()

    answer = input("Do you want to order? (yes/no): ").lower()

    if answer == "yes":
        order = take_order()

        if order:
            print_receipt(order)
        else:
            print("No items were ordered.")

    else:
        print("Thank you! Have a nice day.")


if __name__ == "__main__":
    main()

