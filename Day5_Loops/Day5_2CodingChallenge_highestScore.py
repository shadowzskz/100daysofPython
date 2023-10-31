#Coding Challenge
#Task: check the highest core inside the list
#Input: Student scores
#Output: Heightes score output

from typing import List

stundentNum: int = int(input("How many students? "))
studentScore: List[int] = []
max: int = 0

for datainput in range(0, stundentNum):
    datainput:int = int(input(f"Enter the students height: "))
    studentScore.append(datainput)
    if (datainput>=max):
        max = datainput

print(f"Highest Score of students in list {studentScore} is {max}")