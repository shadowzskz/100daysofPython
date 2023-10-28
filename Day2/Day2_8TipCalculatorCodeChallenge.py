# Code challenge: Tip Calculator
# input: Total Bill, Percentage of Tip, Total People
# Output: Bill for each person
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total Bill? \n"))
tipPercentage:int = 0
while tipPercentage not in [10, 12, 15]:
    tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
totalPeople:int = int(input("How many people to split the bill?\n"))
afterPercentage:float = totalBill*(1+(tipPercentage/100))
afterSplit:float = afterPercentage/totalPeople
bill:float = round(afterSplit, 2)
print(f"Each person should pay: {bill}")