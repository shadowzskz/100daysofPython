#Coding CHallenge
#Task: modify leap year code to return true or false
#input: Year range
#Output: return true or false to check the number of days in that month of year

def checkLeap(year):
    if (year % 4 == 0):
        if (year % 100 >= 1):
            return True
        elif (year % 400 == 0):
            return False
        else:
            return True
    else:
        return False

def checkMonths(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (checkLeap(year) and month==2):
        return 29
    return monthDays[month-1]

def inputUser():
    year: int = int(input("Enter the year to check leap year?\n"))
    month: int = int(input("Enter the month of that year to check no of days?\n"))
    print(checkMonths(year, month))

inputUser()

