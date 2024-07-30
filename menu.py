menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

order_list = []

def add_to_order(item_name, item_price, quantity):
    order_item = {
        "item_name": item_name,
        "item_price": item_price,
        "quantity": quantity
    }
    order_list.append(order_item)

print("Welcome to the variety food truck.")

place_order = True
while place_order:
    print("From which menu would you like to order?")

    i = 1
    menu_items = {}

    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You have selected {menu_category_name}")

            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            menu_item_number = input("Type menu item number: ")

            if menu_item_number.isdigit():
                menu_item_number = int(menu_item_number)

                if menu_item_number in menu_items.keys():
                    item_name = menu_items[menu_item_number]["Item name"]
                    item_price = menu_items[menu_item_number]["Price"]

                    quantity = input("How many would you like to order? ")

                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    add_to_order(item_name, item_price, quantity)

                    print(f"Added {quantity} x {item_name} to your order.")
                else:
                    print(f"{menu_item_number} was not an option.")
            else:
                print("You did not select a valid menu option.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You did not select a number.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        if keep_ordering.lower() == 'y':
            break
        elif keep_ordering.lower() == 'n':
            place_order = False
            print("Thank you for your order!")
            break
        else:
            print("Please type (Y)es or (N)o.")

print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for order in order_list:
    item_name = order["item_name"]
    item_price = order["item_price"]
    quantity = order["quantity"]

    num_item_spaces = 24 - len(item_name)
    num_price_spaces = 6 - len(f"${item_price:.2f}")

    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    print(f"{item_name}{item_spaces} | ${item_price:.2f}{price_spaces} | {quantity}")

total_cost = sum(order["item_price"] * order["quantity"] for order in order_list)
print(f"\nTotal cost: ${total_cost:.2f}")