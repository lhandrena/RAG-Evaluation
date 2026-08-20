# Aufgabe 5: RAG-Optimierungs-Challenge

Zum Abschluss wird es meta: Unsere RAG-Anwendung beantwortet jetzt Fragen über RAG — und du optimierst sie datengetrieben. **RAG über RAG.**

## Lernziele
- Ein RAG-System gegen ein Evaluations-Dataset iterativ und messbar verbessern
- Mehrere Methoden aus dem Training gezielt kombinieren (Chunking, Reranking, Query Expansion, Hybrid Search, ...)
- Mit einem KI-Agenten arbeiten: Du bist der Navigator (Anforderungen und Bewertung), der KI-Agent setzt Änderungen um

## Voraussetzungen
- ✅ Aufgaben 2.1 und 2.2 wurden abgeschlossen (Langfuse läuft, Evaluationspipeline ist bekannt)
- ✅ Die Konzepte aus den Aufgaben 3.x und 4.x (Modelle, Prompts, Chunking, Hybrid Search, Reranking, Query Expansion) sind der Werkzeugkasten für diese Challenge

## Kontext
- **Datenquelle:** 30 gescrapte Web-Dokumente über RAG in [`../src/advanced_rag/scraping/rag_sources/scraped_data/`](../src/advanced_rag/scraping/rag_sources/scraped_data/) — Paper, Blogposts, GitHub-READMEs, aber bewusst auch Rauschen (Tweets, LinkedIn-Posts, Konferenzseiten). Nur ein Teil der Dateien wird vom Dataset abgedeckt — der Rest sind Distraktoren, wie in einem echten Korpus.
- **Evaluations-Dataset:** 20 Fragen in [`../src/advanced_rag/evaluation/datasets/rag_source.csv`](../src/advanced_rag/evaluation/datasets/rag_source.csv)
- Der Branch `rag-challenge` ist der gemeinsame Startpunkt: Skripte, Metriken und Prompt sind bereits vorkonfiguriert.

## Setup (5 Minuten)

1. Branch auschecken. Falls du lokale Änderungen an Code-Dateien hast (z. B. Prompt-Switch aus Aufgabe 3.2 oder `main.py` aus Aufgabe 4.5), lege sie vorher mit `git stash` beiseite (deine `.env` bleibt dabei unangetastet):
```bash
git stash
git fetch && git checkout rag-challenge
```

2. In deiner `.env` die Datenquelle umstellen (die Vektordatenbank muss dafür **nicht** gelöscht werden — jede Quelle bekommt automatisch eine eigene Collection):
```
DOCUMENT_SOURCE=SCRAPED_DATA
```
Stelle außerdem sicher, dass deine `.env` noch der Baseline aus `.env.example` entspricht (u. a. `CHAT_MODEL=gpt-4.1-nano`, `EMBEDDING_MODEL=text-embedding-3-small`, `CHUNKING_STRATEGY=RECURSIVE`, `CHUNK_SIZE=1000`, `CHUNK_OVERLAP=100`, `RETRIEVER_TYPE=SIMILARITY_SEARCH`, `USE_RERANKING=False`) — nur so starten alle vom gleichen Punkt.

3. Backend neu starten (indexiert die neue Quelle automatisch):
```bash
uv run --env-file .env python -m advanced_rag.backend.main
```

4. Das RAG-Dataset nach Langfuse hochladen:
```bash
uv run --env-file .env python src/advanced_rag/evaluation/upload_datasets.py
```

## Teil 1: Baseline messen (10 Minuten)

Führe die Evaluation **zweimal hintereinander** aus, ohne etwas zu ändern:

```bash
uv run --env-file .env python src/advanced_rag/evaluation/evaluate_dataset.py
```

**Optimierungsziel der Challenge sind die Metriken `context_sources_f1` und `faithfulness`.**

**Beobachte in Langfuse (Datasets → rag_source):**
- Wo stehen die Ziel-Metriken? Welche weiteren Metriken sind stark, welche schwach?
- Wie stark schwanken die Werte zwischen den beiden Läufen? Erst Verbesserungen **außerhalb dieser Schwankung** zählen als signifikant (siehe Aufgabe 3.1).
- Welche Fehlermuster erkennst du in den Traces?

## Teil 2: Die Challenge (45-60 Minuten)

Verbessere die Ziel-Metriken, indem du gezielt mehrere Methoden kombinierst. **Mini-Wettbewerb:** Am Ende vergleichen wir die Experimente aller Gruppen in Langfuse — es gewinnt die stärkste signifikante Verbesserung von `context_sources_f1` und `faithfulness` gegenüber der Baseline.

### Arbeitsmodus mit KI-Agent
- **Deine Rolle (Navigator):** Formuliere klare Anforderungen, priorisiere nächste Schritte und definiere Erfolgskriterien
- **Rolle des KI-Agenten:** Führt Änderungen aus, schlägt Varianten vor und setzt Experimente um — die Datei [`AGENTS.md`](../AGENTS.md) im Repo-Root liefert ihm den nötigen Kontext (Befehle, Stellschrauben, Spielregeln)
- **Deine Verantwortung:** Ergebnisse kritisch bewerten (Metriken, Traces, Antwortqualität) und die nächste Iteration entscheiden
- **Sparring:** Nutze den KI-Agenten aktiv, um Hypothesen und einen Schritt-für-Schritt-Plan zu erarbeiten

### Spielregeln
- ⛔ Die Evaluation ist der Schiedsrichter: **Metriken, Eval-Skripte, Dataset und Quelldokumente** (`src/advanced_rag/evaluation/**`, `src/advanced_rag/scraping/**`) **dürfen nicht verändert werden** — auch nicht vom KI-Agenten
- ⛔ Keine Quellen-Dateinamen oder erwarteten Antworten in Prompts oder Code hardcoden
- ✅ Erlaubt ist alles an der Pipeline selbst: Konfiguration, Chunking, Retrieval, Reranking, Prompts, Modelle

### Stellschrauben

| Stellschraube | Wo | Danach nötig |
|---|---|---|
| `CHUNKING_STRATEGY` (`RECURSIVE`, `SEMANTIC`, `SEMANTIC_LLM`), `CHUNK_SIZE`, `CHUNK_OVERLAP` | `.env` | Backend-Neustart (re-indexiert automatisch) |
| `RETRIEVER_TYPE` (`SIMILARITY_SEARCH`, `HYBRID_SEARCH`, `QUERY_EXPANSION`, `QUERY_EXPANSION_LC`) | `.env` | Backend-Neustart |
| `RETRIEVED_NUMBER_OF_DOCUMENTS`, `USE_RERANKING`, `CONTEXT_SIZE_AFTER_RERANKING` | `.env` | Backend-Neustart |
| `CHAT_MODEL` | `.env` | Backend-Neustart |
| `EMBEDDING_MODEL` | `.env` | ⚠️ vorher `rm -rf chroma_langchain_db_*`, dann Backend-Neustart |
| Generierungs-Prompt | [`augmented_generation_prompt.py`](../src/advanced_rag/backend/nodes/prompt_templates/augmented_generation_prompt.py) + `generation_prompt_*.txt` | Backend-Neustart |

### Arbeite iterativ in kurzen Zyklen

Eine Iteration (Änderung → Neustart → Evaluation → Analyse) dauert ca. 10 Minuten — plane also **2-3 saubere Iterationen** ein, statt vieler hektischer.

1. Formuliere mit dem KI-Agenten eine klare Hypothese
2. Lasse die Änderung vom KI-Agenten umsetzen — **möglichst nur einen Hauptfaktor pro Iteration**, damit du Ursache und Wirkung nachvollziehen kannst
3. Führe die Evaluation aus
4. Bewerte das Ergebnis und entscheide den nächsten Schritt

Halte jede Iteration in einem Experiment-Log fest (der Experiment-Name in Langfuse kodiert die Konfiguration):

| # | Hypothese | Änderung | context_sources_f1 | faithfulness | Entscheidung |
|---|---|---|---|---|---|
| 0 | Baseline (2 Läufe) | — | | | |
| 1 | | | | | |
| 2 | | | | | |

## Reflexionsfragen
1. Welche Kombination von Maßnahmen hat den größten Qualitätsgewinn gebracht?
2. Welche Verbesserungen waren messbar, aber inhaltlich kaum relevant (oder umgekehrt)?
3. Wie hat dir der KI-Agent als Sparring-Partner bei Planung und Priorisierung geholfen? Wo musstest du als Navigator bewusst gegen seine Vorschläge entscheiden?
4. Hat dein Agent (bewusst oder unbewusst) versucht, die Metriken zu "gamen" statt das System zu verbessern?
5. **Meta:** Was hast du beim Optimieren dieses RAG-Systems gelernt, das in seinen eigenen Quelldokumenten steht?
