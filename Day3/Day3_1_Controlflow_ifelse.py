# #if else
# syntax
# if condition:
#     do this
# else:
#     do that

#Task: ask height as input
#output: certain height can only do task

print("Welcome to the rolltercoaster")
height: int = int(input("What is your height in cm?\n"))

if (height > 120):
    print("You can go on roller coaster ride")
else:
    print("You are too pudkey to go for roller coaster ride")