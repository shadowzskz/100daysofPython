#coding challenge
# Check how many days, weeks and month left if lived unitl 90 years old.
# input $age

age:int  = input("What is your current age?\n")

leftAge:int = 90 - int(age)
monthLeft:int = leftAge * 12
weekLeft:int = leftAge * 52
dayLeft:int  = leftAge * 365

print(f"Total Months left upto 90 is {monthLeft}, total weeks is {weekLeft} and total days left is {dayLeft}")

