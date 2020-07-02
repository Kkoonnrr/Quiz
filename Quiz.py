from Question import Question

question_prompts = ["what color are apple?\n(A) Red\n(B) Blue\n",
                    "What color are banana?\n(A) Red\n(B) Yellow\n",
                    "What color are pear?\n(A) Red\n(B) Green\n"
                    ]
questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "B")
]
def run_test(questions):
    score = 0
    for ques in questions:
        answer = input(ques.prompt)
        if answer == ques.answer:
            score += 1
    print(score)

run_test(questions)
