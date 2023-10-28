# code challenge
#Task: check if num is odd or even
#input: Number
#output: check number is odd or even using conditions

num: int = int(input("Enter a number to check?\n"))
if(num%2==0):
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")