import uuid
import json
from questions import get_question
from voice_interview import listen_answer
from ai_engine import evaluate_answer

SESSION_FILE = "data/sessions.json"


def start_session(name, company):

    session_id = str(uuid.uuid4())

    session = {
        "session_id": session_id,
        "name": name,
        "company": company,
        "questions": [],
        "score": 0
    }

    save_session(session)

    return session_id


def save_session(session):

    try:
        with open(SESSION_FILE) as f:
            data = json.load(f)
    except:
        data = []

    data.append(session)

    with open(SESSION_FILE, "w") as f:
        json.dump(data, f, indent=2)


def next_question(company):

    return get_question(company)

question = "Explain hash tables"

print("Question:", question)

answer = listen_answer()

feedback = evaluate_answer(question, answer)

print(feedback)

def next_difficulty(current_level, score):

    if score >= 8:

        if current_level == "easy":
            return "medium"

        if current_level == "medium":
            return "hard"

    if score <= 4:

        if current_level == "hard":
            return "medium"

        if current_level == "medium":
            return "easy"

    return current_level