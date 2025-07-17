# QUIZ APP

questions = {"what is the capital of egypt?":"cario",
             "what is 5 * 2 ":"10",
             "what is colour of sun":"white"}
score = 0
for question, answer in questions.items():
    print(question)
    user_answer = input("your answer :").strip()
    if user_answer.lower() == answer.lower():
       print("correct")
       score = score + 1 # or score += 1
    else : 
        print(f"wrong , the correct answer is {answer}")
print(f"\nyour total score :{score}/{len(questions)}")