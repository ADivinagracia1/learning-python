from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Blue\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are blueberries?\n(a) Black\n(b) White\n(c) Orange\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(ask_ques):
    score = 0
    for ques in ask_ques:
        answer = input(ques.prompt)
        if answer == ques.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)