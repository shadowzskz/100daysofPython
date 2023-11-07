#DOCS STRING
print("Doc string is the way to document the code using comments")
print("It is done using three ''' DOc STRING Here ''' ")

def checkLeap(year):
    '''
    :param year:
    :return: if the year is leap year or not using T or F
    '''
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
    '''
    :param year:
    :param month:
    :return: Returns the no of days in each months based on if year is Leap year or not
    '''
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (checkLeap(year) and month==2):
        return 29
    return monthDays[month-1]

def inputUser():
    year: int = int(input("Enter the year to check leap year?\n"))
    month: int = int(input("Enter the month of that year to check no of days?\n"))
    print(checkMonths(year, month))

inputUser()

