"""
Problem 6: Simple Inventory Manager (using Lists and Dictionaries)
Write a Python program that manages a small inventory using a dictionary, where each key is an item name and each value is the quantity in stock.
Requirements:

Start with an empty dictionary to represent the inventory.
Present the user with a menu offering these options, repeated in a loop until the user chooses to exit:

1: Add an item (ask for item name and quantity; if the item already exists, increase its quantity; if not, create it)
2: Remove an item (ask for item name; if it exists, delete it; if not, print a message saying it was not found)
3: View all inventory (print each item and its quantity)
4: Exit the program


Validate user input where reasonable (e.g., quantity must be a positive integer).
Continue looping until the user selects the exit option.

"""



def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item(inventory, item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} has been removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for name, qty in inventory.items():
            print(f"{name}: {qty}")


Inventory = {"Apple": 10}

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View inventory")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_name = input("Enter item name: ").capitalize()
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be a positive number.")
        else:
            add_item(Inventory, item_name, quantity)
            print(f"{item_name} updated. New total: {Inventory[item_name]}")

    elif choice == 2:
        item_name = input("Enter item name: ").capitalize()
        remove_item(Inventory, item_name)

    elif choice == 3:
        view_inventory(Inventory)

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")