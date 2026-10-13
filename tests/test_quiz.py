import unittest
from main import ask_question, run_quiz

class QuizTests(unittest.TestCase):
    def setUp(self):
        self.question = {
            "question": "Two plus two?",
            "options": ["3", "4", "5", "6"],
            "answer": "B",
            "explanation": "Basic arithmetic."
        }

    def test_correct_answer(self):
        outputs = []
        result = ask_question(self.question, 1, 1, input_fn=lambda _: "b", output_fn=outputs.append)
        self.assertTrue(result)

    def test_invalid_then_correct_answer(self):
        answers = iter(["X", "B"])
        outputs = []
        result = ask_question(self.question, 1, 1, input_fn=lambda _: next(answers), output_fn=outputs.append)
        self.assertTrue(result)
        self.assertTrue(any("Invalid input" in line for line in outputs))

    def test_score_summary(self):
        questions = [self.question, {**self.question, "answer": "A"}]
        answers = iter(["B", "B"])
        outputs = []
        result = run_quiz(questions, shuffle=False, input_fn=lambda _: next(answers), output_fn=outputs.append)
        self.assertEqual(result["score"], 1)
        self.assertEqual(result["total"], 2)
        self.assertEqual(result["percentage"], 50.0)

if __name__ == "__main__":
    unittest.main()
