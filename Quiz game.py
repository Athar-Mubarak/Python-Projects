import random

# --- 1. Quiz Data (Standardized for Cleanliness) ---
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Barlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Jupitar", "C. Vanus", "D. Saturn"],
        "answer": "A"
    },
    {
        "question": "What is 7 * 8?",
        "options": ["A. 54", "B. 56", "C. 64", "D. 78"],
        "answer": "B"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    }
]


# ----------------------------------------------------------------------

def run_quiz(quiz_data):
    """
    Runs the command-line quiz, iterates through questions,
    manages scoring, and prints the final results.
    """
    score = 0

    # 🩹 Fixed: Corrected the typo 'random.shufffle' to 'random.shuffle'
    random.shuffle(quiz_data)

    print("--- Welcome to the Python Quiz! ---")
    print("Answer by typing the letter (A, B, C, or D) and pressing Enter.")
    print("-" * 35)

    for q_data in quiz_data:

        # Using .get() with a default value prevents KeyErrors
        # (for 'question', 'options', and 'answer') if the data is slightly malformed.
        question_text = q_data.get('question', '❓ Question Text Missing')
        options = q_data.get('options', [])
        correct_answer = q_data.get('answer', None)

        # Skip questions if critical data is missing
        if not options or not correct_answer:
            print("❌ Error: Critical data missing for this question. Skipping.")
            print("-" * 35)
            continue

        # Display Question and Options
        print(f"\nQuestion: {question_text}")
        for option in options:
            print(option)

        # Get and process user input
        user_answer = input("Your answer: ").strip().upper()

        # Check Answer
        if user_answer == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:

            print(f"Wrong ❌. The correct answer was {correct_answer}.")

        print("-" * 35)

    # --- 2. Final Results (Correctly Indented) ---
    # This block is inside the function, accessing the local variables 'score' and 'quiz_data'.
    total_questions = len(quiz_data)
    print("\n--- Quiz Finished! ---")

    # Calculate and display score summary
    print(f"You answered {score} out of {total_questions} questions correctly.")

    # Prevent ZeroDivisionError if the list was empty, though unlikely here
    if total_questions > 0:
        percentage = (score / total_questions) * 100
        print(f"Your final score is: {percentage:.2f}%")
    else:
        print("No questions were available to display.")


# ----------------------------------------------------------------------

# --- 3. Run Application ---
if __name__ == "__main__":
    run_quiz(questions)