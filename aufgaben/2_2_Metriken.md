# Aufgabe 2.2: Metriken

## Teil 1: Bestehende Metriken aktivieren

- Aktiviere alle Metriken in [`evaluate_dataset.py`](../src/advanced_rag/evaluation/evaluate_dataset.py)
- Führe die Evaluation aus und analysiere die Ergebnisse in Langfuse

## Teil 2: Implementierung einer Wordiness-Metrik

In dieser Übung sollst du eine neue Evaluationsmetrik für das RAG-System implementieren. Die Metrik soll die "Wortigkeit" (Wordiness) von LLM-Antworten bewerten und:

- **1.0** zurückgeben, wenn die Antwort viele Wörter enhält
- **0.0** zurückgeben, wenn die Antwort wenig Wörter enthält

### 1. Implementiere die Metrik

Schau dir die Datei [`wordiness_metric.py`](../src/advanced_rag/evaluation/metrics/wordiness_metric.py) an.

Sie enthält zwei Funktionen:

- eine zum Berechnen der Metrik (`calculate_wordiness_score`)
- eine zum Hochladen der Metrik in Langfuse (`upload_wordiness_metric`)

Implementiere `calculate_wordiness_score` und verstehe `upload_wordiness_metric`.

**Tipp:** 
- Verwende `split()` um Wörter zu zählen

### 2. Teste die neue Metrik

Teste die neue Metrik durch eine Evaluation.

Die Wordiness-Metrik sollte nun in Langfuse erscheinen und korrekte Werte liefern!


### Hilfreiche Ressourcen

- **Beispiel für einfache Metriken:** [`custom_metrics.py`](src/advanced_rag/evaluation/metrics/custom_metrics.py)
- **Beispiel für komplexe Metriken:** [`ragas_metrics.py`](src/advanced_rag/evaluation/metrics/ragas_metrics.py)
- **Upload-Funktion:** [`metric_upload.py`](src/advanced_rag/evaluation/metrics/metric_upload.py)

```
src/advanced_rag/evaluation/
├── metrics/
│   ├── wordiness_metric.py           # NEU: Deine Implementierung
│   ├── custom_metrics.py             # Beispiel
│   ├── ragas_metrics.py              # Beispiel
│   └── metric_upload.py              # Upload-Hilfsfunktion
├── client/
│   └── langfuse_facade.py            # ...
└── evaluate_dataset.py               # Metrik aktivieren
```

### Erfolgskriterien

- ✅ Die Datei `wordiness_metric.py` existiert
- ✅ Die Funktion `calculate_wordiness_score` funktioniert korrekt
- ✅ Die Funktion `upload_wordiness_metric` funktioniert korrekt
- ✅ `MetricsConfig` hat das Feld `use_wordiness`
- ✅ `langfuse_facade.py` nutzt die neue Metrik
- ✅ Die Metrik erscheint in Langfuse nach einer Evaluation


## Teil 3: LLM-as-a-Judge Metrik hinzufügen

In dieser Übung sollst du eine neue **LLM basierte Metrik** verwenden. Die Metrik nutzt Langchain mit structured prompting, um die Qualität von LLM-Antworten zu bewerten.

**Was ist LLM-as-a-Judge?**
Bei diesem Ansatz wird ein LLM verwendet, um die Ausgabe eines anderen LLMs zu bewerten. Das ist besonders nützlich für subjektive Kriterien wie: "Ist die Antwort auf Deutsch?", "Ist die Antwort höflich?", "Ist die Antwort für Jugendliche interessant?"

### 1. Passe den Bewertungs-Prompt an

Die Datei [`llm_judge_metric.py`](../src/advanced_rag/evaluation/metrics/llm_judge_metric.py) enthält bereits die komplette Implementierung. **Deine Aufgabe:** Passe nur den Prompt an!

Öffne die Datei und finde das `JUDGE_PROMPT_TEMPLATE`. Dieses Template definiert, wie das LLM die Antworten bewertet.

**Aktueller Prompt:** Bewertet, ob die Antwort auf Deutsch ist

**Deine Aufgabe:** Ändere den Prompt, sodass er eines der folgenden Kriterien bewertet:
- Ist die Antwort höflich und respektvoll?
- Ist die Antwort für Jugendliche verständlich?
- Ist die Antwort präzise und konkret (ohne unnötige Details)?
- Oder ein eigenes Bewertungskriterium!

**Beispiel:**
```python
JUDGE_PROMPT_TEMPLATE = """
Bewerte die folgende Antwort darauf, ob sie höflich und respektvoll formuliert ist.

Antwort: {llm_reply}

Gib einen Score von 0.0 (unhöflich) bis 1.0 (sehr höflich) zurück.
"""
```

**Hinweis:** Die technische Implementierung (LLM-Aufruf, strukturierte Ausgabe, etc.) ist bereits fertig - du musst nur den Bewertungs-Prompt anpassen!

### 2. Aktiviere die LLM-Judge Metrik

Stelle sicher, dass die Metrik in [`evaluate_dataset.py`](../src/advanced_rag/evaluation/evaluate_dataset.py) aktiviert ist:

```python
# LLM Judge Metric - LLM involved
use_llm_judge: bool = True
```

### 3. Teste die LLM-Judge Metrik

Führe die Evaluation aus, um deine neue Metrik zu testen:

```bash
uv run --env-file .env python src/advanced_rag/evaluation/evaluate_dataset.py
```

Die LLM-Judge-Metrik sollte nun in Langfuse erscheinen und Bewertungen basierend auf deinem angepassten Prompt liefern!