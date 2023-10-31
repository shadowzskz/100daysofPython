import random
import string
from typing import List
letters:List[str] = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
#letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers:List[str] = [str(i) for i in range(10)]
#numbers = list(string.digits)
symbols:List[str] = list(string.punctuation)

print("Welcome to the Password Generator!")
letterNum:int = int(input("How many letters would you like in your password?\n"))
NumNum:int = int(input("How many letters would you like in your password?\n"))
SymbolNum:int = int(input("How many letters would you like in your password?\n"))

randomLetter:List[str] = []
randomNum:List[str] = []
randomSymbol:List[str] = []
for i in range(0, letterNum):
    randomLetter.append(random.choice(letters))

for i in range(0, NumNum):
    randomNum.append(random.choice(numbers))

for i in range(0, SymbolNum):
    randomSymbol.append(random.choice(symbols))


passwords:List[str] = randomLetter + randomNum + randomSymbol
random.shuffle(passwords)
password= ""

for val in passwords:
    password = password + val


# Alternate way
# password = ''.join(passwords)
print(f"Your password is {password}")

