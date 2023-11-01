#Coding Challenge
#Task Prime number checker
#Input: Range of input
#output: Range of Prime Number

from typing import List
def primeNumChecker(range1, range2):
    primeRange: List[int] = []

    for num in range(range1, range2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primeRange.append(num)
    return primeRange

range1: int = int(input("Enter the 1st range: "))
range2: int = int(input("Enter the 2nd range: "))
primeRange = primeNumChecker(range1, range2)
print(primeRange)
