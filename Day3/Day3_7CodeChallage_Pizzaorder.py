#coding challenge
#task: order a pizza and submit bill
# input: Input size of pizza and check if user want additional topping or not
# output: present final bill with price of additional toppping bill added

print("Welcome to te Python Pizza Delieveries!!")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
print("\n")
print("Extra Topping Price")
print("Pepperoni for small Pizze is extra $2")
print("Pepperoni for medium or large Pizze is extra $3")
print("Extra Cheeze for any size Pizze is extra $1")

print("")
size: str = input("What size of Pizza do you want S, M or L?\n")
addPep: str = input("Do you want to add Pepperoni Y or N?\n")
addCheese: str = input("Do you want to add Cheese Y or N?\n")
bill:int = 0
if (size in ["s", "S"]):
    bill = 15
    if(addPep in ["y", "Y"]):
        bill = bill + 2
        if(addCheese in ["y", "Y"]):
            bill = bill + 1
elif (size in ["M", "m"]):
    bill = 20
    if (addPep in ["y", "Y"]):
        bill = bill + 2
        if (addCheese in ["y", "Y"]):
            bill = bill + 1
else:
    bill = 25
    if (addPep in ["y", "Y"]):
        bill = bill + 3
        if (addCheese in ["y", "Y"]):
            bill = bill + 1

print(f"Your {size} pizza price is: {bill}")