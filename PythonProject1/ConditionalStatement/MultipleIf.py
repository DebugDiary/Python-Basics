print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age ? "))
billamt=0
if height >= 120:
    print("You are eligible for the ride")
    if age >18:
        print("You have to pay 17$ ticket price")
        billamt=17
    elif age <=18 and age>=12:
        print("You have to pay 10$ ticket price")
        billamt=10
    else:
        print("You have to pay 7$ ticket price")
        billamt=7
    Photo =input("Do you want a photo? Y/N")
    if Photo == "Y" :
            billamt=billamt+3
    else:
            billamt=billamt*1


else:
    print("Sorry you have to grow taller before you can ride.")
print(f"your bill amount is{billamt}")