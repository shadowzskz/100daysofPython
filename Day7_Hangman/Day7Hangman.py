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
random_wordListDict:dict = {
    'ardvark': 'Nocturnal mammal native to Africa with a long snout and large ears, known for its ability to dig burrows and feed on ants and termites.',
    'baboon': 'Terrestrial monkeys native to Africa and Asia, known for their distinctive appearance, social behavior, and adaptability to various habitats.',
    'camel': 'Large, long-necked mammal native to arid regions of Asia and Africa, known for its humped back and ability to survive in desert conditions.',
    'computer': 'Electronic device designed to perform various tasks such as processing data, storing information, and connecting to the internet.',
    'laptop': 'Portable computer that can be used on the go, typically featuring a keyboard, screen, and built-in battery.',
    'keyboard': 'Input device for computers and typewriters, consisting of keys that allow users to input text and commands.',
    'mouse': 'Pointing device used with computers, typically moved on a surface to control the cursor on the screen.',
    'chair': 'Piece of furniture designed for sitting, typically with a backrest and four legs for support.',
    'table': 'Furniture item with a flat horizontal surface, often used for eating, working, or displaying objects.',
    'door': 'Movable barrier used to open and close entrances to buildings, rooms, or vehicles.',
    'window': 'Opening in a wall or vehicle that is fitted with glass or other transparent material, allowing people to see in or out.',
    'wall': 'Vertical structure that divides or encloses areas, often made of brick, concrete, or other building materials.',
    'floor': 'Horizontal surface of a room on which people walk, typically covered with flooring materials such as carpet, tile, or wood.',
    'apple': 'Round fruit with red or green skin and a whitish interior, often eaten fresh or used in various culinary dishes.',
    'book': 'Written or printed work consisting of pages glued or sewn together along one side and bound with protective covers.',
    'desk': 'Furniture item with a flat surface for working, writing, or reading, often equipped with drawers or compartments for storage.',
    'pen': 'Writing instrument with a thin, pointed tip, usually containing ink, used for writing or drawing on paper.',
    'cat': 'Small domesticated carnivorous mammal, often kept as a pet, known for its independent and playful nature.',
    'dog': 'Domesticated mammal of the species Canis lupus familiaris, known for its loyalty, companionship, and varied breeds.',
    'tree': 'Tall, perennial plant with a single main stem or trunk, typically supporting branches and leaves, and found in various ecosystems.',
    'house': 'Building or structure used as a dwelling for humans, providing shelter, comfort, and privacy.',
    'car': 'Motor vehicle with four wheels, typically powered by an internal combustion engine, used for transportation on roads.',
    'phone': 'Electronic device used for voice communication, text messaging, and accessing the internet, typically portable and wireless.'
}

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

if randomChoice in random_wordListDict:
    hint = random_wordListDict[randomChoice]
    print("Hint for the word")
    print(hint)

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
