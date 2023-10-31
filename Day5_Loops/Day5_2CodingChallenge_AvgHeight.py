#coding exercise
#Tas calculate avg height
#input: List of height
#output: Avg of height

from typing import List

stundentNum: int = int(input("How many students? "))
studentHeight: List[int] = []
sum: int = 0

for datainput in range(0, stundentNum):
    datainput:int = int(input(f"Enter the students height: "))
    studentHeight.append(datainput)
    sum = sum + datainput

print(f"Avgerage height of students in list {studentHeight} is {round(sum/stundentNum)}")