#Coding Challenge
#Task: Cheak if the year is leap year or not
# input: year
# output: tell if that year is leap year or not

year: int = int(input("Enter the year to check leap year?\n"))
if (year%4==0):
    if(year%100>=1):
        print(f"{year} is a leap year")
    elif(year%400==0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")

# startYear: int = int(input("Enter the start year?\n"))
# stopyear: int = int(input("Enter the start year?\n"))
# from typing import List
# leapyear: List[int] = []
# for year in range(startYear, stopyear+1):
#     if (year % 4 == 0):
#         if (year % 100 >= 1):
#             print(f"{year} is a leap year")
#             leapyear.append(year)
#         elif (year % 400 == 0):
#             print(f"{year} is a leap year")
#             leapyear.append(year)
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is not a leap year")
#
# print(f"Leap years betweenn {startYear} and {stopyear} ", leapyear)