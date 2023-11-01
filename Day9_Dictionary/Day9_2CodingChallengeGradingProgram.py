#Coding Challenge
#Task: Grading student based on marks ir 91-100: A
#Input: Student Dictionay Grade
#Output: Grading of Marks

student_score:dict = {}
studentNum:int = int(input("How many Students? "))

for data in range(studentNum):
    studentName:str = input("Enter the student Name: ")
    while not studentName.isalpha():
        print("Please enter alphabets only.")
        studentName:str = input("Enter the student Name: ")

    studentScore = input(f"Enter the score for {studentName}: ")
    while not studentScore.isdigit():
        print("Please enter numeric values only.")
        studentScore = int(input(f"Enter the score for {studentName}: "))
    student_score[studentName] = int(studentScore)

print(f"Your student scores: {student_score}")

print("Converting students scores to grading")
for val in student_score:
    if (student_score[val]>=90):
        student_score[val] = 'OutStanding'
    elif (student_score[val]>=80):
        student_score[val] = 'Exceeds Expectations'
    elif (student_score[val]>=70):
        student_score[val] = 'Acceptable'
    else:
        student_score[val] = 'Fail'

print(f"Your student Grading scores: {student_score}")