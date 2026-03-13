from fastapi import FastAPI
from models import InterviewStart, AnswerSubmit
from interview_engine import start_session, next_question
from ai_engine import evaluate_answer
from webcam_monitor import start_monitor
import threading

app = FastAPI()

@app.get("/")
def home():
    return {"project": "InterviewForge AI Backend Running"}


@app.post("/start-interview")
def start(data: InterviewStart):

    session_id = start_session(data.name, data.company)

    # start webcam monitoring
    threading.Thread(target=start_monitor).start()

    question = next_question(data.company)

    return {
        "session_id": session_id,
        "first_question": question
    }


@app.get("/next-question/{company}")
def next_q(company: str):

    question = next_question(company)

    return {"question": question}


@app.post("/submit-answer")
def submit(data: AnswerSubmit):

    feedback = evaluate_answer(data.question, data.answer)

    return {
        "question": data.question,
        "feedback": feedback
    }