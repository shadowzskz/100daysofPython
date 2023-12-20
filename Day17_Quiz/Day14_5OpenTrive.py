from newquestion_model import Question
from newdata import question_data
from new_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed all the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")