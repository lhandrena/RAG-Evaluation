# Aufgabe 3.2: Prompt-Optimierung

## Lernziele
- Verstehen des Einflusses von Prompt-Qualität auf die RAG-Performance
- Wechselwirkung von Prompt-Qualität und Modellgröße analysieren

## Voraussetzungen
✅ Aufgabe 3.1 (Modell-Optimierung) wurde abgeschlossen

## Teil 1: Prompt-Vergleich mit starkem Modell

### Schritt 1: Aktuellen Prompt analysieren
Öffne die Datei [`augmented_generation_prompt.py`](../src/advanced_rag/backend/nodes/prompt_templates/augmented_generation_prompt.py):

```python
@staticmethod
def get_prompt() -> str:
    prompt_file = Path(__file__).parent / "generation_prompt_bad.txt"
    #prompt_file = Path(__file__).parent / "generation_prompt_good.txt"
    return prompt_file.read_text().strip()
```

Aktuell wird der "bad" Prompt verwendet. Schaue dir beide Prompts an:
- [`generation_prompt_bad.txt`](../src/advanced_rag/backend/nodes/prompt_templates/generation_prompt_bad.txt)
- [`generation_prompt_good.txt`](../src/advanced_rag/backend/nodes/prompt_templates/generation_prompt_good.txt)

**Reflexionsfrage:** Was sind die Hauptunterschiede zwischen den beiden Prompts?

### Schritt 2: Auf "good" Prompt wechseln
Ändere in [`augmented_generation_prompt.py`](../src/advanced_rag/backend/nodes/prompt_templates/augmented_generation_prompt.py):

```python
@staticmethod
def get_prompt() -> str:
    #prompt_file = Path(__file__).parent / "generation_prompt_bad.txt"
    prompt_file = Path(__file__).parent / "generation_prompt_good.txt"
    return prompt_file.read_text().strip()
```

Und wähle als Chat-Modell `gpt-5.2`.

### Schritt 3: Backend neu starten und evaluieren
- Backend neu starten
- Evaluation durchführen (evaluate_dataset.py)

### Schritt 4: Metriken vergleichen
Analysiere in Langfuse:
- Wie haben sich die Metriken durch den besseren Prompt verändert?
- Welche Metriken profitieren am meisten?
- Gibt es überraschende Verschlechterungen?

## Teil 2: Prompt-Impact bei schwächerem Modell

### Schritt 5: Auf schwächeres Modell wechseln
Öffne die [`.env`](../.env) Datei und wechsel auf `gpt-4.1-nano`

### Schritt 6: Erneute Evaluation mit gutem Prompt
- Backend neu starten
- Evaluation durchführen (evaluate_dataset.py)

### Schritt 7: Prompt-Impact vergleichen
Vergleiche in Langfuse die folgenden Konfigurationen:
1. **gpt-5.2 + bad prompt** (aus Aufgabe 3.1)
2. **gpt-5.2 + good prompt** (aus Teil 1)
3. **gpt-4.1-nano + good prompt** (aktuell)

**Analysefragen:**
- Wie groß ist der Prompt-Impact bei gpt-5.2?
- Wie groß ist der Prompt-Impact bei gpt-4.1-nano?

### Reflexionsfragen
1. Warum kann ein kleineres Modell mit besserem Prompt ein größeres Modell mit schlechtem Prompt übertreffen?
2. Welche Rolle spielt die Prompt-Qualität im Vergleich zur Modellgröße?
3. Wann lohnt sich der Einsatz eines größeren Modells?

## Teil 3 (Optional): Rules aus dem Prompt entfernen

- Öffne [`generation_prompt_good.txt`](../src/advanced_rag/backend/nodes/prompt_templates/generation_prompt_good.txt) und entferne die "Rules" am Ende des Prompts.
- Vergleiche gpt-5.2 mit und ohne "Rules"?


## Fazit: Erkenntnisse aus Aufgabe 3.1 und 3.2

### Modell-Optimierung (3.1)
- ✅ Modelle (LLM & Embedding-Modell) zu variieren ist technisch einfach
- ⚠️ Größere LLMs sind nicht immer besser
- ✅ Bei Embedding-Modellen lohnen sich größere Modelle meistens
- 💡 LLMs bei RAG "formulieren" hauptsächlich um - nicht übertreiben

### Prompt-Optimierung (3.2)
- ✅ Prompts zu variieren ist technisch einfach
- ⚠️ Impact ist oft begrenzt, aber messbar
- 💡 Gute Prompts können schwächere Modelle kompensieren
- ⚠️ Bei Prompts nicht übertreiben - Einfachheit ist oft besser

### Wichtige Erkenntnisse
1. **Kosten-Nutzen-Abwägung:** Größere Modelle kosten mehr, bringen aber nicht immer proportional bessere Ergebnisse
2. **LLM vs. Retrieval:** Die Retrieval-Qualität ist oft wichtiger als das LLM
