import os
from services.questions import load_questions, calculate_scores
from services.analysis import generate_radar_chart, save_summary

def ask_questions(questions):
    """
    Mostra le 20 domande e raccoglie le risposte dell'utente (scala 1-5).
    """
    answers = {}
    print("Rispondi alle seguenti domande (1 = per niente d'accordo, 5 = totalmente d'accordo):\n")
    for q in questions:
        while True:
            try:
                val = int(input(f"{q['id']}) {q['text']} (1-5): "))
                if 1 <= val <= 5:
                    answers[q["id"]] = val
                    break
                else:
                    print("Inserisci un numero da 1 a 5.")
            except ValueError:
                print("Valore non valido. Inserisci un numero da 1 a 5.")
    return answers

if __name__ == "__main__":
    # Percorsi di output (si assicura che esistano le cartelle)
    os.makedirs("docs", exist_ok=True)

    # Carica le domande
    questions = load_questions()

    # Chiede le risposte
    answers = ask_questions(questions)

    # Calcola i punteggi per categoria
    scores = calculate_scores(questions, answers)

    # Genera grafico e report
    generate_radar_chart(scores)
    save_summary(scores)

    print("\n--- QUESTIONARIO COMPLETATO ---")
    print("Report generato in: docs/report_summary.txt")
    print("Grafico generato in: docs/report_chart.png")
