import os
from services.questions import load_questions

OUTPUT_HTML = "docs/test.html"

HTML_HEADER = """<!DOCTYPE html>
<html lang='it'>
<head>
    <meta charset='utf-8'>
    <title>Questionario di Coaching</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .question { margin-bottom: 1em; }
    </style>
</head>
<body>
<h1>Questionario completo</h1>
<form>
"""

HTML_FOOTER = """
<button type='submit'>Invia</button>
</form>
</body>
</html>
"""

def generate_html(questions):
    parts = [HTML_HEADER]
    for q in questions:
        parts.append(f"<div class='question'>\n<p>{q['id']}) {q['text']}</p>")
        for i in range(1, 6):
            parts.append(f"<label><input type='radio' name='q{q['id']}' value='{i}'> {i}</label>")
        parts.append("</div>\n<hr>")
    parts.append(HTML_FOOTER)
    return "\n".join(parts)

if __name__ == "__main__":
    os.makedirs('docs', exist_ok=True)
    questions = load_questions()
    html = generate_html(questions)
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML generato in {OUTPUT_HTML}")
