import random
# import NumberManipulation
#
# Random_int=random.randint(1,10)
# print(Random_int)
# print(NumberManipulation.NumberIJK)

random_0to1=int(random.random()*10)
if random_0to1 % 2 == 0:
    print("Heads")
else:
    print("Tails")