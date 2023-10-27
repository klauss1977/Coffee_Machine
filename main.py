MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    """Prepares the drink and calculates remaining resources"""
    water = MENU[drink]['ingredients']['water']
    coffee = MENU[drink]['ingredients']['coffee']
    if drink != 'espresso':
        milk = MENU[drink]['ingredients']['milk']
        if milk > resources['milk']:
            print("Sorry there is not enough milk.")
            return
        resources['milk'] -= milk
    if water > resources['water']:
        print("Sorry there is not enough water.")
        return
    elif coffee > resources['coffee']:
        print("Sorry there is not enough coffee.")
        return
    resources['water'] -= water
    resources['coffee'] -= coffee
    print(f"Here is your {drink} ☕ . Enjoy!")
    return resources


shutdown = False
while not shutdown:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print(f"""Water: {resources['water']} ml
Milk: {resources['milk']} ml
Coffee: {resources['coffee']} g
Money: $""")
    elif order == 'exit':
        shutdown = True
    else:
        make_drink(order)

print(resources)
