#code Challenge
#Input two digit number and result should be sum of that two digit number
# 23 output should be 2 + 3
num: str = "0"
while (len(num)!=2):
    num = input("Emter any two digit number: ")

firstDigit:int = int(num[0])
secondDigit:int = int(num[1])
if (type(firstDigit)==int and type(secondDigit)==int):
    print ("Result is ", firstDigit + secondDigit)

