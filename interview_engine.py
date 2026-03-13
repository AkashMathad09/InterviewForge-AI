import uuid
import json
from questions import get_question

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