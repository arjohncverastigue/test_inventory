inventory = {}


def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    print(f"Added {quantity} of '{name}'.")


def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Removed '{name}' from inventory.")
    else:
        print(f"Item '{name}' not found.")


def update_stock(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print(f"Updated '{name}' stock to {quantity}.")
    else:
        print(f"Item '{name}' not found.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for name, quantity in inventory.items():
            print(f"{name}: {quantity}")
        print()


def main():
    while True:
        print("\nSimple Inventory Manager - Crujido")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Stock")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            add_item(name, qty)
        elif choice == '2':
            name = input("Item name to remove: ")
            remove_item(name)
        elif choice == '3':
            name = input("Item name to update: ")
            qty = int(input("New quantity: "))
            update_stock(name, qty)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
