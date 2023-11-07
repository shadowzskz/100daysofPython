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
    num1:int  = int(input("Enter your first Number: "))
    num2:int  = int(input("Enter your second Number: "))
    for operator in operations:
        print(operator)
    operator: str = input("What is your operator?: ")
    choseFun = operations[operator]
    result = choseFun(num1, num2)
    print(f"The result of {num1} {operator} {num2} is {result}")

inputUser()

