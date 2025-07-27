# Testcoaching

Questo progetto è pensato per creare una piattaforma di coaching e sviluppo personale, capace di valutare le competenze trasversali e tecniche di un individuo attraverso un questionario strutturato.
L’obiettivo è aiutare a definire un profilo personale completo, utile sia per la crescita individuale che per contesti aziendali (recruitment, valutazione interna, piani di formazione).

## Indice della Struttura del Progetto

```
Testcoaching/
│
├── app/
├── services/
│   ├── questions.py
│   ├── analysis.py
│
├── data/
│   └── questions.json
│
├── docs/
│   (qui saranno salvati il report e il grafico)
│
├── run_test.py
├── generate_html.py
└── README.md


```

> **Nota:** Aggiorna l’indice se aggiungi o rimuovi file importanti.

Il file `data/questions.json` contiene 100 domande suddivise in sei categorie: leadership, intelligenza_emotiva, ottimismo, soft_skills, hard_skills e problem_solving.

Per ottenere una versione HTML del questionario esegui:

```bash
python generate_html.py
```

Il file risultante `docs/test.html` potrà essere aperto con qualsiasi browser e stampato o distribuito.
