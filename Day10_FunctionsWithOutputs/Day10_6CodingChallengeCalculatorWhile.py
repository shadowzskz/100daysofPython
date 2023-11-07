#CODING CHALLENGE
#TASK: Make Calculator
#INPUT: Numbers
#OUTPUT: Calculated Number

import pyfiglet

def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2


operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }
def inputUser():
    print(pyfiglet.figlet_format("Welcome to the Basic Calculator"))
    condition:bool = True
    while (condition):
        num1: int = int(input("Enter your first Number: "))
        num2: int = int(input("Enter your second Number: "))
        for operator in operations:
            print(operator)
        operator: str = input("What is your operator?: ")
        choseFun = operations[operator]
        result = choseFun(num1, num2)
        print(f"The result of {num1} {operator} {num2} is {result}")
        checkCon: str = (input("Do you want to continur or exit Type Y or N: ")).lower()
        numofCod = ['y','n']
        while(checkCon not in numofCod):
            if (checkCon.lower() == 'n'):
                break
            elif (checkCon.lower() == 'y'):
                checkCon = True
            else:
                print("Press Valid num")
                checkCon: str = (input("Do you want to continur or exit Type Y or N: ")).lower()
            condition=False
        print(pyfiglet.figlet_format("Thankyou for using"))
inputUser()

