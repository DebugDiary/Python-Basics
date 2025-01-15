import art
choice = input("What would you like? (espresso/latte/cappuccino):")
def check_resources(lmao):
    for i in art.resources:
        if art.resources[i]<art.MENU[lmao]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")



check_resources(choice)