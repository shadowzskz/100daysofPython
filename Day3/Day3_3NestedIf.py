#Nested Ifelse
#syntax
# if condition:
#     if another condition:
#         do this
#     else:
#         do that
# else:
#     do this instead

print("Welcome to the rolltercoaster")
height: int = int(input("What is your height in cm?\n"))
age: int = int(input("What is your Age?\n"))

if (height > 120):
    print("Your height is enough for roller coaster ride")
    if (age<7):
        print("You can ride free")
    elif (age<=18):
        print("You need to pay to go on ride")
    else:
        print("but you are too old fuchey for rollercoaster")
else:
    print("You are too pudkey to go for roller coaster ride")