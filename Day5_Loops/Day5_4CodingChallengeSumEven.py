#CODING CHALLENGE
#input: range of numbers
#output: sum of even num between the range
print("Sum of number between range:")
range1:int = int(input("Input the 1st range: "))
range2:int = int(input("Input the 2nd range: "))
sum:int = 0
for num in range(range1-1, range2+1,2):
    sum = sum + num

print(f"The sum of numbers between {range1} and {range2} is: {sum}")