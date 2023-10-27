numChar = len(input("What is your name? "))
print(type(numChar))
#converting to string
print("Converting to string")
newNumChar = str(numChar)
print("new Type type(newNumChar)", type(newNumChar), newNumChar)

#convert int to float type
intNum = 123
print(intNum, type(intNum))
print(float(intNum), type(float(intNum)))

#convert string to float
print("10 + float('123.1')", 10 + float("123.1"))