#Coding Challenge
#input: input a range
#output
# if num is divided by 3 then print "FIZZ"
# if num is divided by 5 then print "BUZZ"
# if num is divided by 3 and 5 then print "FIZZBUZZ"

print("Fizz BuZZ:")
range1:int = int(input("Input the 1st range: "))
range2:int = int(input("Input the 2nd range: "))

for fizzbuzz in range(range1, range2+1):
    if (fizzbuzz%3==0 and fizzbuzz%5==0):
        print("FIZZ")
    elif (fizzbuzz%3==0):
        print("BUZZ")
    elif(fizzbuzz%5==0):
        print("FIZZBUZZ")
    else:
        print(fizzbuzz)