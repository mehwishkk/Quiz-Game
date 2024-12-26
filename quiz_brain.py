class QuizBrain():
    def __init__(self,Question_list):
        self.q_number = 0
        self.question_list = Question_list
        self.score=0

    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number +=1
        user_input=input(f"Q{self.q_number}: {current_question.text} (True?False)").capitalize()
        self.check_ans(user_input,current_question.answer)

    def still_has_question(self):
        if self.q_number+1 <=  len(self.question_list):
            return True

    def check_ans(self, user_input,correct_answer):
        if user_input == correct_answer:
            self.score =self.score+1
            print("You are correct")
            print("you score:",self.score)
        else:
            print("You are wrong")

        print(f"your score: {self.score}/{self.q_number}")
        print(' \n')

