#FUNCTIONS
# Syntax
# FUNCTION WITH no INPUTS
# def myFun():
#     Do something
#
# FUNCTION WITH INPUTS
# def myFun(some input):
#     Do something with some input
#
# FUNCTION WITH OUTPUT
# def myFun():
#    return  doingSomething

def myFun():
    return 3*2

print(myFun())

def formatedName(fName, lName):
    formattedFname = fName.title()
    formattedLname = lName.title()
    return f"{formattedFname} {formattedLname}"

print(formatedName("SAHAJ", "SHAKYA"))
