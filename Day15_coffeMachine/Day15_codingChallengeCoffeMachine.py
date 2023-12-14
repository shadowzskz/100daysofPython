from data import *
def isSuffiecent(order):
    """Returns order status"""
    for item in order:
        if (order[item] >= resources[item]):
            print(f"Sorry there is not enough {item}")
            return False
    return True

def processcoins():
    """Returns total calculated amount"""
    print("Please insert coins")
    total = int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.1
    total += int(input("How many nickles? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total

def isTransactionSuccess(moneyRec, drinkCost):
    """Returns if money is accepted or not"""
    if (moneyRec >=drinkCost):
        change = round(moneyRec - drinkCost,2)
        print(f"Here is your change: {change}")
        global profit
        profit +=drinkCost
        return True
    else:
        print("Sorry that's nor enough money. Money Refunded")
        return False

def makeCoffe(drinkName, orderIngrident):
    """Deduct Ingirdent"""
    for item in orderIngrident:
        resources[item] -= orderIngrident[item]
    print(f"Here is your {drinkName} ☕")

profit = 0
is_on = True
while is_on:
    choice = input("What do you want? espresso, latte, cappuccino : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if (isSuffiecent(drink["ingredients"])):
            payment = processcoins()
            data = isTransactionSuccess(payment, drink["cost"])
            if (data==False):
                print(f"Money refund is {payment}")

            makeCoffe(choice, drink["ingredients"])
