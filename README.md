# Testcoaching

Benvenuto nel repository **Testcoaching**!

## Indice della Struttura del Progetto

```
profilo-utente/
├── README.md            # Descrizione del progetto, uso e contributi
├── .gitignore           # File/directory da ignorare da Git
├── app/
│   ├── main.py          # Entry point dell'applicazione FastAPI
│   ├── models.py        # Definizione delle classi (utente, risposte, profilo)
│   ├── schemas.py       # Schemi pydantic per validazione input/output
│   ├── api/
│   │   ├── endpoints.py # API REST (start questionnaire, answer, profile)
│   └── services/
│       ├── questions.py # Logica per selezione domande adattive
│       ├── analysis.py  # Logica di analisi e punteggio risposte
│       └── profiling.py # Generazione del report finale
├── data/
│   ├── questions.json   # Archivio di domande con metadati (categoria, peso)
│   └── examples/
│       └── responses.json # Esempi di risposte per test
├── docs/
│   └── design.md        # Documentazione tecnica e di processo
├── tests/
│   ├── test_api.py      # Test dei vari endpoint
│   └── test_analysis.py # Test della logica di analisi/profilazione
├── scripts/
│   └── populate_db.py   # Script per importare domande nel DB
└── requirements.txt     # Dipendenze Python
```

> **Nota:** Aggiorna l’indice se aggiungi o rimuovi file importanti.

## Altre informazioni

- [Documentazione tecnica](docs/design.md)
- Per domande o suggerimenti, apri una issue!
