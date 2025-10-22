# Aufgabe 2.1: Evaluierungsplattformen

## Lernziele
- Langfuse als Evaluierungsplattform kennenlernen
- Datensätze hochladen und Evaluationen durchführen
- Traces, Datasets und Dashboards in Langfuse verstehen
- Detaillierte Analyse einzelner Traces durchführen

## Voraussetzungen
- Abgeschlossenes Setup (Aufgabe 1)


## Teil 1: Datensatz hochladen (5 Minuten)
Lade einen Test-Datensatz in Langfuse hoch, führe dazu einfach das folgende Skript aus:

```bash
uv run --env-file .env python src/advanced_rag/evaluation/upload_datasets.py
```

**Beobachte:**
- Welche Datensätze werden hochgeladen?
- Wo erscheinen sie in Langfuse?


## Teil 2: Evaluation durchführen (10 Minuten)

Führe eine Evaluation mit dem hochgeladenen Datensatz durch, dazu musst du das `evaluate_dataset.py` Skript ausführen. Dieses verwendet den zuvor hochgeladenen Datensatz, sendet die Fragen einzeln ans Backend und berechnet Metriken.

```bash
uv run --env-file .env python src/advanced_rag/evaluation/evaluate_dataset.py
```
(oder run-config "evaluate_dataset" ausführen)


**Beobachte:**
- Welche Metriken werden berechnet?
- Wo sehe ich die Evaluation-Ergebnisse in Langfuse?


## Teil 3: Einzelne Traces analysieren (5 Minuten)

Wähle einen Trace aus und analysiere ihn im Detail:

**Finde heraus:**
- Wo sehe ich den ursprünglichen Prompt?
- Wo finde ich den abgerufenen Kontext (Retrieved Documents)?
- Wo ist die generierte Antwort?
- Welche Zwischenschritte gibt es?


## Optional: Dashboards
- Welche vorgefertigten Dashboards gibt es?
- Welche Insights liefern sie?
- Kann ich eigene Dashboards erstellen?
