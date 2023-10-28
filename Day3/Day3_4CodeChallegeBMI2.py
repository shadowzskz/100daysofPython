#code challenge
#task: BMI CALCULATOR
# input: height and weight
# output: result with interpretation

# Calculate BMI
# BMI = weight/((height)^2)

height: float = float(input("Enter your Height In meter? \n"))
weight: float = float(input("Enter your Weight in KG? \n"))

bmi = round((weight)/(height**2),2)

print("Your BMI is: ", bmi)

if (bmi <= 18.5):
    print("You are underweight")
elif (bmi<=25):
    print("You are normal")
elif (bmi<=30):
    print("You are overweight")
elif (bmi<=35):
    print("You are Obese")
else:
    print("You are clinically obese")