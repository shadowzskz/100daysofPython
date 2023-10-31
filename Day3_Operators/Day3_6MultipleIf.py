#Multiple If
#syntax
# if condition1:
#    do this
# if condition2:
#    do this
# if conditon3:
#    do that

print("Welcome to the rolltercoaster")
height: int = int(input("What is your height in cm?\n"))
age: int = int(input("What is your Age?\n"))

if (height > 120):
    print("Your height is enough for roller coaster ride")
    if (age<7):
        bill = 0
        print("You can ride free")
        print("Your bill is: ", bill)
    elif (age<=18):
        bill = 5
        print("You need to pay to go on ride")
        print("Your bill is: ", bill)
    else:
        bill = 10
        print("but you are too old fuchey for rollercoaster need to pay adult price")
        print("Your bill is: ", bill)
    wantPhoto = input("Do you want to click photo? Y or N\n")
    if (wantPhoto == "Y" or wantPhoto == "y"):
        bill = bill + 3

    print("Your total bill is: ", bill)
else:
    print("You are too pudkey to go for roller coaster ride")