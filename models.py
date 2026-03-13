from pydantic import BaseModel

class InterviewStart(BaseModel):
    name: str
    company: str

class AnswerSubmit(BaseModel):
    session_id: str
    question: str
    answer: str