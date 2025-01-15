import sys
import art

money=0
cond=True

def makeCoffee():
    for i in art.resources:
        art.resources[i] =art.resources[i]- art.MENU[choice]["ingredients"][i]
    print(f"Here is your {choice} ☕ Enjoy!")

def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    total_money= float((0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*pennies))
    if total_money >= art.MENU[choice]["cost"]:
        print(f"Here is ${total_money-art.MENU[choice]["cost"]} in change")
        global money
        money=money+art.MENU[choice]["cost"]
        makeCoffee()
    else:
        print("Sorry there is not enough money. Money refunded")

def check_resources(choice):
    for i in art.resources:
        if art.resources[i]<art.MENU[choice]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True

while cond:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        sys.exit()

    elif choice == "report":
        for key in art.resources:
            print(f"{key}: {art.resources[key]}{art.units[key]}")
        print(f"money: {money}{art.units["cost"]}")
    elif choice =="espresso" or choice =="latte" or choice =="cappuccino":
        if check_resources(choice):
            process_coins()
        else:
            cond=True
    else:
        print("Sorry , this flavour is unavailable , we will take your suggestion, Thank you :) !")
