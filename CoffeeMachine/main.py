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

# Global Variables
money = 0

# TODO: 3. Print report.


def report(dict_resources):
    """ A report should be generated that shows the current resource values """
    for key in dict_resources:
        if key == "coffee":
            print(f"{key.capitalize()}: {dict_resources[key]}g")
        else:
            print(f"{key.capitalize()}: {dict_resources[key]}ml")
    print(f"Money: ${money}")

# TODO: 4. Check resources sufficient?


def check_resources(drink, dict_resources, dict_menu):
    """ return ok if there are sufficient resources for the drink """
    out_resource = ""
    if drink == "espresso":
        if dict_resources["water"] < dict_menu[drink]["ingredients"]["water"]:
            out_resource = "water"
        elif dict_resources["coffee"] < dict_menu[drink]["ingredients"]["coffee"]:
            out_resource = "coffee"
        else:
            return "ok"
    elif drink == "latte" or drink == "cappuccino":
        if dict_resources["water"] < dict_menu[drink]["ingredients"]["water"]:
            out_resource = "water"
        elif dict_resources["coffee"] < dict_menu[drink]["ingredients"]["coffee"]:
            out_resource = "coffee"
        elif dict_resources["milk"] < dict_menu[drink]["ingredients"]["milk"]:
            out_resource = "milk"
        else:
            return "ok"
    return out_resource


# TODO: 5. Process coins.


def insert_coins():
    """ Prompt the user to insert coins and return the total value inserted """
    quarters_val = 0.25
    dimes_val = 0.10
    nickles_val = 0.05
    pennies_val = 0.01
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_val = (quarters * quarters_val) + (dimes * dimes_val) + (nickles * nickles_val) + (pennies * pennies_val)
    return round(total_val, 2)

# TODO: 6. Check transaction successful?


def check_transaction(drink, value, dict_menu):
    """ Check that the user has inserted enough money to purchase the drink they selected. """
    # refer to global variable 'money' inside function
    global money
    if value < dict_menu[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money += dict_menu[drink]["cost"]
        if value > dict_menu[drink]["cost"]:
            change = round(value - dict_menu[drink]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
        return True

# TODO: 7. Make Coffee.


def make_coffee(drink, dict_resources, dict_menu):
    if drink == "latte" or drink == "cappuccino":
        dict_resources["water"] -= dict_menu[drink]["ingredients"]["water"]
        dict_resources["milk"] -= dict_menu[drink]["ingredients"]["milk"]
        dict_resources["coffee"] -= dict_menu[drink]["ingredients"]["coffee"]
    else:
        dict_resources["water"] -= dict_menu[drink]["ingredients"]["water"]
        dict_resources["coffee"] -= dict_menu[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink}. Enjoy!")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.


turn_off = False
while not turn_off:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino)"
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        turn_off = True
    elif choice == "report":
        report(resources)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resource_ok = check_resources(choice, resources, MENU)
        if resource_ok == "ok":
            val = insert_coins()
            if check_transaction(choice, val, MENU):
                make_coffee(choice, resources, MENU)
        else:
            print(f"Sorry there is not enough {resource_ok}")
