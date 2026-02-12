# Aufgabe 5: RAG über RAG

## Lernziele
- Einen RAG-spezifischen Datensatz in Langfuse hochladen und evaluieren
- Die RAG-Anwendung durch Kombination mehrerer Methoden verbessern
- Mit einem KI-Agenten arbeiten: Du bist der Navigator (Anforderungen und Bewertung), der KI-Agent setzt Änderungen um


## Voraussetzungen
- ✅ Aufgaben 2.1 und 2.2 wurden abgeschlossen
- ✅ Backend und Evaluationspipeline laufen lokal

## Kontext
- Quellen zum Thema RAG liegen in [`../src/advanced_rag/scraping/rag_sources/scraped_data/`](../src/advanced_rag/scraping/rag_sources/scraped_data/)
- Das passende Evaluations-Dataset liegt in [`../src/advanced_rag/evaluation/datasets/rag_source.csv`](../src/advanced_rag/evaluation/datasets/rag_source.csv)

## Arbeitsmodus mit KI-Agent
- **Deine Rolle (Navigator):** Formuliere klare Anforderungen, priorisiere nächste Schritte und definiere Erfolgskriterien
- **Rolle des KI-Agenten:** Führt Änderungen aus, schlägt Varianten vor und setzt Experimente um
- **Deine Verantwortung:** Ergebnisse kritisch bewerten (Metriken, Traces, Antwortqualität) und die nächste Iteration entscheiden
- **Sparring beim Experimentieren:** Nutze den KI-Agenten aktiv, um Hypothesen und einen Schritt-für-Schritt-Plan für das weitere Vorgehen zu erarbeiten

## Teil 1: RAG-Dataset hochladen (5 Minuten)

- Öffne [`../src/advanced_rag/evaluation/upload_datasets.py`](../src/advanced_rag/evaluation/upload_datasets.py) und stelle sicher, dass `rag_source.csv` als Quelle verwendet wird.
- Führe dann den Upload aus


## Teil 2: Evaluation mit dem RAG-Dataset (10 Minuten)

- Starte das Evaluations-Skript evaluate-dataset.py mit dem neuen Datensatz

**Beobachte:**
- Welche Metriken sind stark, welche schwach?
- Welche Fehlermuster erkennst du in den Traces?

## Teil 3: RAG-System verbessern (20-30 Minuten)

Verbessere die Anwendung, indem du gezielt mehrere Methoden kombinierst (z. B. Chunking, Reranking, Query Expansion, Hybrid Search, ...).

Arbeite iterativ in kurzen Zyklen:
1. Formuliere mit dem KI-Agenten eine klare Hypothese
2. Lasse die Änderung vom KI-Agenten umsetzen
3. Führe die Evaluation aus
4. Bewerte Ergebnis und entscheide den nächsten Schritt

**Wichtig:** Ändere pro Iteration möglichst nur einen Hauptfaktor, damit du Ursache und Wirkung nachvollziehen kannst.

## Reflexionsfragen
1. Welche Kombination von Maßnahmen hat den größten Qualitätsgewinn gebracht?
2. Welche Verbesserungen waren messbar, aber inhaltlich kaum relevant (oder umgekehrt)?
3. Wie hat dir der KI-Agent als Sparring-Partner bei Planung und Priorisierung geholfen?
4. Wo musstest du als Navigator bewusst gegen Vorschläge des KI-Agenten entscheiden?
