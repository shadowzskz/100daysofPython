#coding exercise
#Task: Head or tail coin toss

import random
from typing import List
toss: List[str] = ['Head', 'Tails']
userInput: str = ''
while(userInput.lower()!='n'):
    userInput: str = input("Do you want to toss the coin? Y or N: ")
    if (userInput.lower() == 'y'):
        result: int = random.randint(0, 1)
        print(f"You got {toss[result]}")
else:
    print("Thankyou for playing")