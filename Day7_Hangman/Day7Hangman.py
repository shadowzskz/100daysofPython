#Step 1
#Task: Pick random word

import random
from typing import List
import pyfiglet
import string

random_wordList:List[str] = ["ardvark", "baboon", "camel", "computer", "laptop",
                             "keyboard", "mouse", "chair", "table", "door", "window",
                             "wall", "floor", "apple", "book", "desk", "pen", "cat",
                             "dog", "tree", "house", "car", "phone"]
randomChoiceInt:int = random.randint(0, len(random_wordList)-1)
randomChoice:str = random_wordList[randomChoiceInt]
wordLen:int = len(randomChoice)
guess:bool = False
count:int = 0
displayVal:str = '_' * wordLen
hangman:str =  ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

userInputList:[str] = []
print(pyfiglet.figlet_format("Welcome to HangMan"))

while(guess!=True):
    print(displayVal)
    if (len(userInputList)!=0):
        print(f"You have guessed {userInputList}")
    inpUser:str = input("Guess the letter: ")
    while (len(inpUser)!=1 or inpUser.isnumeric() or inpUser.isspace() or inpUser in list(string.punctuation)):
        print("Please re enter")
        inpUser: str = input("Guess the letter: ")

    if inpUser in userInputList:
        print("You have already added that")
    else:
        if inpUser in randomChoice:
            for val in range(wordLen):
                if inpUser == randomChoice[val]:
                    displayVal = displayVal[:val] + inpUser + displayVal[val + 1:]
                    if (displayVal == randomChoice):
                        result = pyfiglet.figlet_format("You won")
                        print(result)
                        guess = True

        else:
            print("In correct Guess")
            print(hangman[count])
            count = count + 1;
            choiceLeft = len(hangman) - count
            if (count == len(hangman)):
                result = pyfiglet.figlet_format("You Lose")
                print(result)
                guess = True
            else:
                print("Try again")
                print(f"You have {choiceLeft} left")

    userInputList.append(inpUser)

print("Thankyou for playing")
