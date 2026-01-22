print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step_1 = input("You're at a cross road. Where do you want to go?\n Type left or right:\n").lower()

if step_1 == "left":
    step_2 =input('''You've come to a lake. There is an island in the middle of the lake.
  Type "wait" to wait for a boat. \nType "swim" to swim across.\n''').lower()
    if step_2 == "wait":
        step_3 = input('''You arrive at the island unharmed. \nThere is a house with 3 doors.
  One red, one yellow and one blue. Which colour do you choose?\n''').lower()
        if step_3 == "yellow":
            print("You found the treasure! You Win!")
        elif step_3 == "blue":
            print("It is a room full of fire. game over!")
        elif step_3 ==  "red":
            print("It is a room full of beasts. game over!")
    elif step_2 == "swim":
        print("You were attacked by a shark, game over!")
elif step_1 == "right":
    print("Yow were attacked by a dragon, game over!")
else:
    print("you cannot go there")
