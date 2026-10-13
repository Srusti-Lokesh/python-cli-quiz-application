# Python CLI Quiz Application

A beginner-friendly multiple-choice quiz project built with Python and JSON. It includes a terminal-based quiz (the core assignment) and an optional Flask web interface so the project can also be hosted on Render.

## Features

- 12 questions stored separately in `quiz_app/questions.json`
- Randomized question order in the CLI and web versions
- Validates answers and handles invalid CLI input
- Immediate feedback and explanations
- Automatic score and percentage calculation
- Final performance summary
- Automated unit tests
- Optional responsive Flask web UI for Render deployment

## Requirements

- Python 3.10 or newer recommended
- Internet connection only for installing the optional web dependencies and deploying

## Run the CLI quiz (Windows PowerShell)

```powershell
# 1. Extract the ZIP, then move into the project folder
cd .\cli_quiz_application

# 2. Create a virtual environment
py -m venv .venv

# 3. Activate it
.\.venv\Scripts\Activate.ps1

# If PowerShell blocks activation, use this for the current terminal only:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Then run activation again.

# 4. Install dependencies only if you plan to run the web version
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 5. Run the required CLI app
python main.py

# 6. Run tests
python -m unittest discover -s tests -v
```

The CLI itself uses only the Python standard library; Flask/Gunicorn are for the optional hosted web interface.

## Run the web version locally

```powershell
python app.py
```

Open `http://127.0.0.1:5000` in your browser. Stop the server with `Ctrl+C`.

## Deploy the web version to Render

Render cannot provide an interactive terminal session for a conventional CLI app as a public website. For that reason, this repository includes a small web interface using the same JSON question bank.

1. Push this repository to GitHub.
2. Sign in to Render and connect your GitHub account.
3. Choose **New + → Web Service** and select this repository.
4. Use these settings (or let `render.yaml` configure them):
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Ensure `SECRET_KEY` is set as an environment variable. `render.yaml` requests a generated value.
6. Create the service and wait for the deploy to finish.
7. Open the `onrender.com` URL and test Start quiz, answer validation, and the result screen.

The Render web deployment hosts the optional browser version; `python main.py` remains the assignment's command-line deliverable. Free-instance availability and sleep behavior can change by Render plan/policy.

## GitHub submission (PowerShell)

Create a new **public** repository on GitHub named `python-cli-quiz-application`. Add the description:

> A Python command-line quiz application using JSON question data, randomized questions, input validation, score calculation, and a final performance summary. Includes an optional Flask web interface for Render deployment.

When creating the repository, do not initialize it with a README, `.gitignore`, or license because this project already contains files for those.

Then run these commands from the project folder, replacing `YOUR-USERNAME` with your GitHub username:

```powershell
git --version
git init
git add .
git commit -m "Build Python CLI quiz application"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-cli-quiz-application.git
git push -u origin main
```

If Git asks you to identify yourself:
```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
Use the email you want associated with your Git commits. For GitHub authentication, follow the browser/device login flow prompted by Git Credential Manager; do not put a password or token directly in your commands.

If `origin` already exists, check it with `git remote -v`. If it points to the wrong repository, update it:
```powershell
git remote set-url origin https://github.com/YOUR-USERNAME/python-cli-quiz-application.git
```

## Suggested submission checklist

- [ ] Run `python main.py` and complete a quiz
- [ ] Run `python -m unittest discover -s tests -v` and confirm all tests pass
- [ ] Verify `quiz_app/questions.json` has at least 10 questions
- [ ] Push all project files to a public GitHub repository
- [ ] Add the deployed Render URL to the README after deployment
- [ ] Add the GitHub repository URL to the README
- [ ] Submit the repository URL through the internship portal
- [ ] Post the completed project on LinkedIn, as required by the brief

## Project structure

```text
cli_quiz_application/
├── main.py
├── app.py
├── quiz_app/
│   ├── __init__.py
│   └── questions.json
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── question.html
│   └── result.html
├── tests/
│   └── test_quiz.py
├── requirements.txt
├── Procfile
├── render.yaml
├── .gitignore
├── README.md
└── REPORT.pdf
```

## Technologies

- Python: quiz logic, functions, loops, validation, scoring
- JSON: external question bank
- Flask: optional web interface
- Gunicorn: production WSGI server for Render
- Git and GitHub: version control and source-code submission
- Render: hosting for the optional web interface
