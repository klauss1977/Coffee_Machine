MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_drink(drink):
    """Prepares the drink, deducts the required ingredients from resources and calculates remaining resources if the
    payment is processed successfully."""
    water = MENU[drink]['ingredients']['water']
    coffee = MENU[drink]['ingredients']['coffee']
    milk = MENU[drink]['ingredients']['milk']
    if water > resources['water']:
        print("Sorry there is not enough water.")
        return
    elif milk > resources['milk']:
        print("Sorry there is not enough milk.")
        return
    elif coffee > resources['coffee']:
        print("Sorry there is not enough coffee.")
        return
    print("Please insert coins.")
    if process_coins(drink):
        resources['water'] -= water
        resources['milk'] -= milk
        resources['coffee'] -= coffee
        print(f"Here is your {drink} ☕ . Enjoy!")


def process_coins(product):
    """Processes the inserted coins and compares it with the cost of the product.
    Returns True if the value of the coins inserted is greater or equal to the cost.
     Calculates the change if the value of the coins is greater than the cost."""
    # quarter = 0.25
    # dime = 0.1
    # nickel = 0.05
    # penny = 0.01
    cost = MENU[product]["cost"]
    try:
        quarter = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickel = int(input("how many nickles?: "))
        penny = int(input("how many pennies?: "))
    except ValueError:
        print(f"You inserted a type of coin that is not accepted. Try again.")
        return False
    amount = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    if amount < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(amount - cost, 2)
        print(f"Here is ${change} in change.")
        resources['money'] += cost
        return True


shutdown = False
resources['money'] = 0

while not shutdown:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'report':
        print(f"""Water: {resources['water']} ml
Milk: {resources['milk']} ml
Coffee: {resources['coffee']} g
Money: ${resources['money']}""")
    elif order == 'exit':
        shutdown = True
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        make_drink(order)
    else:
        print(f"You entered '{order}', which is not correct. Please, try again.")
