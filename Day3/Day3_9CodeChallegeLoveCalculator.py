#coding Exercise
#love calculator
#Task: Get 1st and last name of two people
    # Check how many True Love characher exist on both name
#OutputL display percentage

print("Welcome to the Love Calculator!")
name1: str = ""
name2: str = ""
while(name1==""):
    name1: str = input("What is your name? ")
while(name2==""):
    name2: str = input("What is your partners name? ")

name1 = name1.lower()
name2 = name2.lower()

countT:int = name1.count('t') + name2.count('t')
countR:int = name1.count('r') + name2.count('r')
countU:int = name1.count('u') + name2.count('u')
countE:int = name1.count('e') + name2.count('e')

countTrue = countT + countR + countU + countE

countL:int = name1.count('l') + name2.count('l')
countO:int = name1.count('o') + name2.count('o')
countV:int = name1.count('v') + name2.count('v')
countE1:int = name1.count('e') + name2.count('e')

countLove = countL+ countO + countV + countE1

total = int(str(countTrue)+ str(countLove))

if (total<=10 or total>90):
    print(f"Your score is {total}, you go like coke and mentos.")
elif (total>=40 and total<=50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")