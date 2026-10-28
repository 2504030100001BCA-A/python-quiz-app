
import json


class Quiz:
    def __init__(self, name):
        self.name = name
        self.score = 0

        self.questions = [
            {
                "question": "Which keyword is used to create a function in Python?",
                "options": ("A. loop", "B. def", "C. class", "D. return"),
                "answer": "B"
            },
            {
                "question": "Which data type stores key-value pairs?",
                "options": ("A. list", "B. tuple", "C. dictionary", "D. set"),
                "answer": "C"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ("A. #", "B. //", "C. @", "D. &"),
                "answer": "A"
            },
            {
                "question": "Which keyword is used to handle an exception?",
                "options": ("A. if", "B. for", "C. try", "D. def"),
                "answer": "C"
            },
            {
                "question": "Which method converts a string to lowercase?",
                "options": ("A. upper()", "B. lower()", "C. strip()", "D. split()"),
                "answer": "B"
            }
        ]

    def start_quiz(self):
        print("\nWelcome to the Python Quiz!")
        print("Answer each question using A, B, C or D.\n")

        for number, question_data in enumerate(self.questions, start=1):
            print(f"Question {number}: {question_data['question']}")

            for option in question_data["options"]:
                print(option)

            while True:
                answer = input("Your answer: ").strip().upper()

                if answer in ("A", "B", "C", "D"):
                    break
                else:
                    print("Please enter A, B, C or D.")

            if answer == question_data["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print("Wrong!")
                print("Correct answer:", question_data["answer"], "\n")

    def show_result(self):
        total = len(self.questions)
        percentage = (self.score / total) * 100

        print("=" * 30)
        print("QUIZ RESULTS")
        print("=" * 30)
        print("Player:", self.name)
        print("Score:", self.score, "/", total)
        print(f"Percentage: {percentage:.1f}%")

        if percentage >= 80:
            print("Great job!")
        elif percentage >= 50:
            print("Good effort! Keep practising.")
        else:
            print("Keep learning and try again!")

        self.save_result(percentage)

    def save_result(self, percentage):
        result = {
            "name": self.name,
            "score": self.score,
            "total_questions": len(self.questions),
            "percentage": round(percentage, 1)
        }

        try:
            with open("quiz_results.json", "r") as file:
                results = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            results = []

        results.append(result)

        try:
            with open("quiz_results.json", "w") as file:
                json.dump(results, file, indent=4)
            print("\nYour result has been saved!")
        except OSError:
            print("\nCould not save your result.")


def main():
    print("=== Python Quiz Application ===")

    name = input("Enter your name: ").strip()

    if name == "":
        name = "Student"

    quiz = Quiz(name)
    quiz.start_quiz()
    quiz.show_result()


main()
