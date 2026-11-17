questions = [
    "Language in this course?",
    "Keyword for a condition?",
    "What is 2 + 3?",
]
answers = ["python", "if", "5"]
score = 0
quit_quiz = False

for index in range(len(questions)):
    print(questions[index])
    for attempt in range(2):
        answer = input("Answer, or q to quit: ").strip().lower()
        if answer == "q":
            quit_quiz = True
            break
        if answer == answers[index]:
            score = score + 1
            print("Correct")
            break
        print("Not correct")
    if quit_quiz:
        break

print(f"Score: {score}/{len(questions)}")
