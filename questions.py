import random

questions = {
    "google": [
        "Explain hash tables",
        "What is Big-O complexity?",
        "Difference between process and thread?",
        "Design a URL shortener"
    ],
    "amazon": [
        "Explain REST API",
        "What is load balancing?",
        "Explain scalability",
        "Design a shopping cart system"
    ],
    "hr": [
        "Tell me about yourself",
        "What are your strengths?",
        "Describe a challenge you faced"
    ]
}

def get_question(company):
    company = company.lower()

    if company in questions:
        return random.choice(questions[company])

    return random.choice(questions["hr"])