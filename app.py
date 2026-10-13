"""Optional Flask web interface for deployment on Render."""
import json
import os
from pathlib import Path
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "development-only-change-me")
QUESTIONS_PATH = Path(__file__).parent / "quiz_app" / "questions.json"

def load_questions():
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as file:
        questions = json.load(file)
    return questions

@app.get("/")
def index():
    return render_template("index.html", count=len(load_questions()))

@app.post("/start")
def start():
    questions = load_questions()
    session["order"] = list(range(len(questions)))
    import random
    random.shuffle(session["order"])
    session["position"] = 0
    session["score"] = 0
    session["answers"] = []
    return redirect(url_for("question"))

@app.get("/question")
def question():
    order = session.get("order")
    if not order:
        return redirect(url_for("index"))
    position = session.get("position", 0)
    if position >= len(order):
        return redirect(url_for("result"))
    item = load_questions()[order[position]]
    return render_template("question.html", item=item, number=position+1, total=len(order))

@app.post("/answer")
def answer():
    order = session.get("order")
    if not order:
        return redirect(url_for("index"))
    position = session.get("position", 0)
    if position >= len(order):
        return redirect(url_for("result"))
    questions = load_questions()
    item = questions[order[position]]
    selected = request.form.get("answer", "").upper()
    if selected not in {"A", "B", "C", "D"}:
        return render_template("question.html", item=item, number=position+1,
                               total=len(order), error="Choose one of the four options.")
    correct = selected == item["answer"]
    session["score"] = session.get("score", 0) + int(correct)
    answers = session.get("answers", [])
    answers.append({"selected": selected, "correct": correct})
    session["answers"] = answers
    session["position"] = position + 1
    return redirect(url_for("question"))

@app.get("/result")
def result():
    order = session.get("order")
    if not order:
        return redirect(url_for("index"))
    total = len(order)
    score = session.get("score", 0)
    percentage = round(score / total * 100, 2) if total else 0
    if percentage >= 80:
        message = "Excellent work!"
    elif percentage >= 50:
        message = "Good effort. Keep practicing!"
    else:
        message = "Keep learning and try again!"
    return render_template("result.html", score=score, total=total,
                           percentage=percentage, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
