import json
from collections import defaultdict

# Percorso del file con le domande
QUESTIONS_FILE = "data/questions.json"

def load_questions():
    """Carica le domande dal file JSON."""
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def collect_answers(questions):
    """
    Simula la raccolta delle risposte.
    In un’app reale, qui arriveranno input da un form o API.
    """
    answers = {}
    for q in questions:
        # Simulazione: assegna a tutte le risposte un valore fisso (es. 3 su 5)
        answers[q["id"]] = 3
    return answers

def calculate_scores(questions, answers):
    """
    Calcola il punteggio per ciascuna categoria.
    """
    scores = defaultdict(int)
    for q in questions:
        q_id = q["id"]
        score = answers.get(q_id, 0) * q.get("weight", 1)
        scores[q["category"]] += score
    return dict(scores)

def generate_report(scores):
    """
    Crea un report sintetico in base ai punteggi.
    """
    report = "\nProfilo della persona:\n"
    for category, score in scores.items():
        report += f"- {category.capitalize()}: {score} punti\n"
    return report

if __name__ == "__main__":
    questions = load_questions()
    answers = collect_answers(questions)
    scores = calculate_scores(questions, answers)
    print(generate_report(scores))
