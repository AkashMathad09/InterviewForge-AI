import random

questions = {
    "google": [
        "Explain hash tables",
        "What is Big-O complexity?",
        "Difference between process and thread?",
        "Explain REST API"
    ],

    "amazon": [
        "What is load balancing?",
        "Explain microservices architecture",
        "Explain CAP theorem"
    ],

    "hr": [
        "Tell me about yourself",
        "What are your strengths?",
        "Why should we hire you?"
    ]
}


def get_question(company):

    company = company.lower()

    if company in questions:
        return random.choice(questions[company])

    return random.choice(questions["hr"])