# Author: Nandith Reddy Malapati

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

game_items = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors:\n "))
computer_choice = random.randint(0,2)

print("Player Chose", player_choice)
print(game_items[player_choice])
print("Computer Chose", computer_choice)
print(game_items[computer_choice])

if player_choice == computer_choice:
    print("Its a draw!")
elif ((player_choice == 1 and computer_choice == 0) or
      (player_choice == 2 and computer_choice == 1) or
        (player_choice == 0 and computer_choice == 2)):
    print("You win!")
else:
    print("You lose!")
