import json
import matplotlib.pyplot as plt
import numpy as np
from services.questions import load_questions, collect_answers, calculate_scores

# Nome file di output
OUTPUT_IMAGE = "docs/report_chart.png"
OUTPUT_TEXT = "docs/report_summary.txt"

def generate_radar_chart(scores):
    """
    Genera un grafico radar delle categorie con punteggi.
    """
    categories = list(scores.keys())
    values = list(scores.values())
    
    # Chiude il grafico riportando il primo valore alla fine per chiudere il cerchio
    values += values[:1]
    N = len(categories)

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Disegna i bordi e le etichette
    plt.xticks(angles[:-1], categories)
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.25)

    plt.title("Profilo della persona", size=16)
    plt.savefig(OUTPUT_IMAGE)
    plt.close()
    print(f"Grafico salvato in {OUTPUT_IMAGE}")

def save_summary(scores):
    """
    Salva un report testuale con i punteggi.
    """
    lines = ["Profilo della persona (punteggi per categoria):\n"]
    for category, score in scores.items():
        lines.append(f"- {category.capitalize()}: {score} punti")
    summary_text = "\n".join(lines)

    with open(OUTPUT_TEXT, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print(f"Report testuale salvato in {OUTPUT_TEXT}")

if __name__ == "__main__":
    questions = load_questions()
    answers = collect_answers(questions)
    scores = calculate_scores(questions, answers)

    generate_radar_chart(scores)
    save_summary(scores)
