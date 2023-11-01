#CODING CHALLENGE
#TASK: AREA CALCULATION
#input: height and width
#output: Number of paint cant needed (1 can can paint 5sqm of wall)
import math


def paintCan(height, width):
    coverage: int = 5
    print(f"1 paint can can paint {coverage} sq meter of wall")
    canNec: float = round((height * width) / 5,2)
    return  canNec


height: int = int(input("Enter the height of the wall: "))
width: int = int(input("Enter the width of the wall: "))

canNec = paintCan(height,width)
print(f"No of cans needed are:  {canNec}")
