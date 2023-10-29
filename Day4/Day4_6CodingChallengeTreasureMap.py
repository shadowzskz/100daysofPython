#Code Challenge
#task: there are blank tiles on list
#input: input list col and row position where to put the treasure
#output: return array with treasure marked X

from typing import List
row1: List[int] = ["0", "0", "0"]
row2: List[int] = ["0", "0", "0"]
row3: List[int] = ["0", "0", "0"]

map: List[int] = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
pos = input("Where do you want to place the treasure? ")
colVal: int = int(pos[0])-1
rowval:int = int(pos[1])-1
map[rowval][colVal]= "X"
print(f"{row1}\n{row2}\n{row3}")