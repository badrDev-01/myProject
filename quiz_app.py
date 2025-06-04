questions = [
    {
    "question": "What is the output of 'print(2**3)'?",
    "options": ["6", "8", "9", "4"],
    "answer": "8"
},

{"question": "Which keyword is used to define a function in Python?",
 "options": ["func", "def", "function", "lambda"],
 "answer": "def"
 },

{
    "question": "What does 'len([1,2,3,4])' return?",
    "options": ["3", "4", "5", "None"],
    "answer": "4"
},

{"question": "Which data type is immutable in Python?",
 "options": ["List", "Dictionary", "Tuple", "Set"],
 "answer": "Tuple"
 },

{"question": "How do you start a comment in Python?",
 "options": ["//", "#", "/*", "--"],
 "answer": "#"
 }]


def run_quiz():
    score = 0

    print("Welcome to the Python Quiz! Answer the following questions:")
    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        # Get user's answer
        try:
            user_choice = int(input("Enter the number of your answer: "))
            if q["options"][user_choice - 1] == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("⚠️ Invalid choice. Please enter a valid number next time.")

    print(f"\nQuiz Completed! Your final score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()