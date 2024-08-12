class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0


    def still_has_questions(self):

        if self.question_number<len(self.question_list):
            return True
        else: return False





    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(current_question)
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text}(True(False)?:\n")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct):
        if user_answer.lower()==correct.lower():
            self.score += 1
            print("Rrrighhhtttt!")
            print(f"Your current score:{self.score}/{self.question_number}")

        else:
            print(f"That's Wrong. Your current score:{self.score}/{self.question_number}")
        print(f"The correct answer was: {correct}")
        print("\n")