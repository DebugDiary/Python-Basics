print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age ? "))

if height >= 120:
    print("You are eligible for the ride")
    if age >18:
        print("You have to pay 17$ ticket price")
    elif age <=18 and age>=12:
        print("You have to pay 10$ ticket price")
    else:
        print("You have to pay 7$ ticket price")
else:
    print("Sorry you have to grow taller before you can ride.")