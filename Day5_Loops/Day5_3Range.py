#Range

print("Print the num in range")
for num in range(1,10):
    print(num)

print("Print the num in range with step of 2")
for num in range(1,10,2):
    print(num)

print("Print the num in range with step of 3")
for num in range(1,10,3):
    print(num)

print("Sum of number between range:")
range1:int = int(input("Input the 1st range: "))
range2:int = int(input("Input the 2nd range: "))
sum:int = 0
for num in range(range1, range2+1):
    sum = sum + num

print(sum)