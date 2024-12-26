from question_model import Question # question class
from data import question_data # question dict
from quiz_brain import QuizBrain
#print(question_data)
q1 = Question("2+3=5","True")
#print(q1.text)

question_bank = []


for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_q1 = Question(question_text,question_ans)
    question_bank.append(new_q1)

qb=QuizBrain(question_bank)
while qb.still_has_question()==True:
    qb.next_question()

print(f"Your final score is: {qb.score}/{len(question_bank)}")
