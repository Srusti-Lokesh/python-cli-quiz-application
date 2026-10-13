"""Command-line quiz application. Run with: python main.py"""
import json
import random
from pathlib import Path

QUESTIONS_PATH = Path(__file__).parent / "quiz_app" / "questions.json"

def load_questions(path=QUESTIONS_PATH):
    """Load and validate questions from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        questions = json.load(file)
    if not isinstance(questions, list) or not questions:
        raise ValueError("The question bank must be a non-empty JSON list.")
    required = {"question", "options", "answer"}
    for number, item in enumerate(questions, start=1):
        if not required.issubset(item):
            raise ValueError(f"Question {number} is missing required fields.")
        if len(item["options"]) != 4 or item["answer"] not in {"A", "B", "C", "D"}:
            raise ValueError(f"Question {number} must have four options and answer A-D.")
    return questions

def ask_question(question, number, total, input_fn=input, output_fn=print):
    """Display a multiple-choice question and return whether the answer is correct."""
    output_fn(f"\nQuestion {number}/{total}: {question['question']}")
    for index, option in enumerate(question["options"]):
        output_fn(f"  {chr(65 + index)}. {option}")
    while True:
        answer = input_fn("Your answer (A/B/C/D): ").strip().upper()
        if answer in {"A", "B", "C", "D"}:
            break
        output_fn("Invalid input. Please enter A, B, C, or D.")
    correct = answer == question["answer"]
    if correct:
        output_fn("Correct!")
    else:
        output_fn(f"Not quite. Correct answer: {question['answer']}. {question['options'][ord(question['answer']) - 65]}")
    if question.get("explanation"):
        output_fn(f"Explanation: {question['explanation']}")
    return correct

def run_quiz(questions=None, shuffle=True, input_fn=input, output_fn=print):
    """Run the quiz and return a result summary."""
    questions = list(questions if questions is not None else load_questions())
    if shuffle:
        random.shuffle(questions)
    score = 0
    output_fn("=" * 48)
    output_fn("          PYTHON KNOWLEDGE QUIZ")
    output_fn("=" * 48)
    for number, question in enumerate(questions, start=1):
        if ask_question(question, number, len(questions), input_fn, output_fn):
            score += 1
    percentage = round((score / len(questions)) * 100, 2) if questions else 0.0
    output_fn("\n" + "=" * 48)
    output_fn("                 QUIZ RESULTS")
    output_fn("=" * 48)
    output_fn(f"Score: {score}/{len(questions)}")
    output_fn(f"Percentage: {percentage:.2f}%")
    if percentage >= 80:
        output_fn("Performance: Excellent!")
    elif percentage >= 50:
        output_fn("Performance: Good effort. Keep practicing!")
    else:
        output_fn("Performance: Keep learning and try again!")
    output_fn("=" * 48)
    return {"score": score, "total": len(questions), "percentage": percentage}

def main():
    try:
        run_quiz()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Unable to start quiz: {error}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
