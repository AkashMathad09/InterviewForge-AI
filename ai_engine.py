def evaluate_answer(question, answer):

    score = min(len(answer) // 20, 10)

    return {
        "score": score,
        "strength": "Answer attempts to address the question",
        "improvement": "Add more technical explanation and examples"
    }