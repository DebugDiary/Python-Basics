import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS=[rock,paper,scissors]
user_choice=int(input(("What do you want to choose ? type 0 for rock,1 for paper , 2 for scissors\n")))
print(f"You chose: \n{RPS[user_choice]}")
computer_no=random.randint(0,2)
computer_choice=RPS[computer_no]
print(f"Computer chose:\n {computer_choice}")

# Check who wins
if user_choice == computer_no:
    print("It's a draw!")
elif (user_choice == 0 and computer_no == 2) or \
        (user_choice == 1 and computer_no == 0) or \
        (user_choice == 2 and computer_no == 1):
    print("You win!")
else:
    print("You lose!")
