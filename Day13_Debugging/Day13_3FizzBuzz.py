#Coding Challenge
#Debuggin FIzz Buzz

for fizzbuzz in range(1, 101):
    if (fizzbuzz%3==0 and fizzbuzz%5==0):
        print("FIZZ")
    elif (fizzbuzz%3==0):
        print("BUZZ")
    elif(fizzbuzz%5==0):
        print("FIZZBUZZ")
    else:
        print(fizzbuzz)