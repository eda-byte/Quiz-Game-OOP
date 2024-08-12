from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
question_bank = []
for item in question_data:
    #print(item)  # Debugging: Check each item

    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(question_data)

while quiz.still_has_questions():
      quiz.next_question()

print(f"You've completed the quiz.\n"
     f"Final score was: {quiz.score}/{quiz.question_number}")