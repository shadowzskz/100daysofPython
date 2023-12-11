#coding challenge
#task: Play rock paper scissors with computer
#input: chose rock paper scissors
#ouput: win or loose

import random
from typing import List;
rock: str = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper: str = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors: str = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice: List[str] = [rock, paper, scissors]

userCHoice: int = int(input("Enter your choice 0 for Rock, 1 for Paper and 2 for scissors? "))
print("You chose:")
print(choice[userCHoice])
print("Computer choose:")
ai:int = random.randint(0,2)
print(choice[ai])
if (userCHoice == 0 and ai == 2):
    print("You won")
elif (userCHoice > ai):
    print("You won")
elif (userCHoice==ai):
    print("Draw")
else:
    print("You lose")

