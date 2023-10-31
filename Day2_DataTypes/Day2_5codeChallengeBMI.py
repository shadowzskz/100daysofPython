#Code Challenge
# Calculate BMI
# BMI = weight/((height)^2)

height: float = float(input("Enter your Height In meter? \n"))
weight: float = float(input("Enter your Weight in KG? \n"))

bmi = (weight)/(height**2)

print("Your BMI is: ", bmi)