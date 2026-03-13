from fastapi import FastAPI
import threading

from questions import get_question
from ai_engine import evaluate_answer
from voice_interview import listen_answer
from webcam_monitor import start_monitor
from confidence_analysis import analyze_confidence

app = FastAPI()

# store current question globally
current_question = ""


@app.get("/")
def home():
    return {"project": "InterviewForge AI Backend Running"}


# START INTERVIEW
@app.post("/start-interview")
def start_interview():

    global current_question

    try:
        threading.Thread(target=start_monitor, daemon=True).start()
        print("Webcam started")
    except Exception as e:
        print("Webcam monitor failed:", e)

    try:
        current_question = get_question("google")
        print("Question generated:", current_question)
    except Exception as e:
        print("Question generation failed:", e)
        return {"error": "Question system failed"}

    return {
        "message": "Interview started",
        "question": current_question
    }


# VOICE ANSWER
@app.get("/voice-answer")
def voice_answer():

    global current_question

    answer = listen_answer()

    feedback = evaluate_answer(current_question, answer)

    return {
        "question": current_question,
        "answer": answer,
        "feedback": feedback
    }


# NEXT QUESTION
@app.get("/next-question/{company}")
def next_q(company: str):

    global current_question

    current_question = get_question(company)

    return {"question": current_question}


# SUBMIT TEXT ANSWER
@app.post("/submit-answer")
def submit(data: dict):

    question = data["question"]
    answer = data["answer"]

    feedback = evaluate_answer(question, answer)

    return {
        "question": question,
        "feedback": feedback
    }


# FINISH INTERVIEW
@app.post("/finish-interview")
def finish_interview():

    confidence_score = analyze_confidence()

    return {
        "technical_score": 7.5,
        "communication_score": 8.1,
        "confidence_score": confidence_score,
        "integrity_score": 94
    }


# RESULTS DASHBOARD
@app.get("/results")
def results():

    return {
        "technical_score": 7.5,
        "communication_score": 8.1,
        "confidence_score": 82,
        "integrity_score": 94,
        "weak_questions": [
            "Explain hash tables",
            "Explain load balancing"
        ]
    }


# AI MENTOR PRACTICE
@app.post("/mentor-practice")
def mentor_practice(data: dict):

    question = data["question"]
    answer = data["answer"]

    feedback = evaluate_answer(question, answer)

    return {
        "mentor_feedback": feedback
    }