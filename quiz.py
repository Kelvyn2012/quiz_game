questions = (
    "What is the capital city of Australia?: ",
    "Who wrote the play Romeo and Juliet?: ",
    "Which planet is known as the Red Planet?: ",
    "How many continents are there in the world?: ",
    "What is the chemical symbol for gold?",
)
options = (
    ("A. Sydney", "B. Melbourne", "C. Canberra ", "D. Perth"),
    (
        "A. Charles Dickens",
        "B. William Shakespeare",
        "C. Jane Austen",
        "D. George Orwell",
    ),
    (
        "A. Earth",
        "B. Jupiter",
        "C. Venus",
        "D. Mars",
    ),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Gd", "B. Au", "C. Ag", "D. Go"),
)
answers = ("C", "B", "D", "C", "B")
guesses = []
question_num = 0
score = 0
for question in questions:
    print(".............................")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Kindly choose between (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"the correct answer is {answers[question_num]}")

    question_num += 1

print(".............................")
print("   RESULT    ")
print(".............................")

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
    
print()

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
