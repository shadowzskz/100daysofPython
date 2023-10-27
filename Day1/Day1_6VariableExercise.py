#Aim to switch the values of variables
# initial values stored as a and b
# Swap a and b

a: str = input("A is: ")
b: str = input("B is: ")

#Swap using a temp
temp: str = a
a = b
b = temp

#After Swap
print ("Data after swaping a and b")
print ("A: ",a,"B: ", b)