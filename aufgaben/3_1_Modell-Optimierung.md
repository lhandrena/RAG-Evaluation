# Aufgabe 3.1: Modell-Optimierung

## Lernziele
- Verstehen des Einflusses verschiedener Embedding-Modelle auf die RAG-Performance
- Analysieren der Auswirkungen unterschiedlicher Chat-Modelle auf die Antwortqualität
- Systematisches Evaluieren und Vergleichen von Modell-Konfigurationen
- Interpretation von Metriken in Langfuse

## Voraussetzungen
✅ Das [`evaluate_dataset`](../src/advanced_rag/evaluation/evaluate_dataset.py) Script wurde mindestens einmal mit allen Metriken aktiviert ausgeführt

## Teil 1: Baseline-Stabilität verstehen

### Schritt 1: Mehrfache Evaluationen ohne Änderungen
Bevor wir Optimierungen vornehmen, ist es wichtig zu verstehen, wie stabil unsere Metriken sind. Führe die Evaluation 2 oder 3 mal hintereinander aus, **ohne irgendetwas zu verändern**.

### Schritt 2: Metrik-Schwankungen analysieren
Öffne Langfuse und vergleiche die Ergebnisse der mehrfachen Evaluationen:

**Zu beobachtende Aspekte:**
- Welche Metriken schwanken zwischen den Durchläufen?
- Wie stark sind die Schwankungen (in Prozent)?
- Welche Metriken bleiben stabil?

**Typische Beobachtungen:**
- **Retrieval-Metriken** (Context Precision, Context Recall): Meist sehr stabil, da deterministisch
- **LLM-basierte Metriken** (Faithfulness, Answer Relevancy): Können leicht schwanken durch nicht-deterministische LLM-Antworten
- **Generierte Antworten**: Können bei gleicher Frage unterschiedlich formuliert sein

### Reflexionsfragen
1. Ab welcher Schwankung würdest du eine Verbesserung als "signifikant" betrachten?
2. Wie viele Evaluationen bräuchte man für statistisch robuste Aussagen?

**Wichtig:** Diese Baseline-Messungen helfen dir später zu entscheiden, ob Änderungen tatsächlich Verbesserungen bringen oder nur im Rahmen der normalen Schwankung liegen.

## Teil 2: Embedding-Modell Optimierung

### Schritt 1: Vektordatenbank zurücksetzen
Die Vektordatenbank muss gelöscht werden, damit sie mit dem neuen Embedding-Modell neu erstellt wird.

**Ordnername:** `chroma_langchain_db_<chunk_size>_<overlap>`
- Beispiel: `chroma_langchain_db_1000_100` (Chunk-Size: 1000, Overlap: 100)
- Die Zahlen können je nach Konfiguration variieren

**Option 1: Manuell löschen**
- Navigiere zum Projektverzeichnis
- Lösche den Ordner `chroma_langchain_db_*` manuell

**Option 2: Per Terminal**
```bash
# Lösche die Vektordatenbank
rm -rf chroma_langchain_db_*
```

Die Datenbank wird beim nächsten Start des Backends automatisch mit dem neuen Embedding-Modell neu erstellt.

### Schritt 2: Embedding-Modell wechseln
Öffne die [`.env`](../.env) Datei und ändere:
```
# Vorher:
EMBEDDING_MODEL=text-embedding-3-small

# Nachher:
EMBEDDING_MODEL=text-embedding-3-large
```

**Hintergrund:** `text-embedding-3-large` erzeugt höherdimensionale Embeddings (3072 vs 1536 Dimensionen), was zu präziseren semantischen Repräsentationen führen kann.

### Schritt 3: Backend neu starten und Evaluation durchführen
- Backend neu starten
- Evaluation durchführen (evaluate_dataset.py)

### Schritt 4: Metriken vergleichen
Analysiere in Langfuse:
- Wie haben sich die Retrieval-Metriken verändert?
- Gibt es Verbesserungen bei der Relevanz der abgerufenen Dokumente?
- Hat sich die Antwortqualität verbessert?

**Reflexionsfragen:**
- Warum könnte ein größeres Embedding-Modell bessere/schlechtere Ergebnisse liefern?
- Welche Trade-offs gibt es (Performance, Kosten, Qualität)?

## Teil 3: Chat-Modell Optimierung

### Schritt 5: Chat-Modell wechseln
Öffne die [`.env`](../.env) Datei und ändere:
```
# Vorher:
CHAT_MODEL=gpt-4.1-nano

# Nachher:
CHAT_MODEL=gpt-5
```

**Hintergrund:** Neuere/größere Modelle haben oft besseres Reasoning und können komplexere Zusammenhänge verstehen.

### Schritt 6: Erneute Evaluation
```bash
# Führe die Evaluation mit dem neuen Chat-Modell aus
python src/advanced_rag/evaluation/evaluate_dataset.py
```

### Schritt 7: Finale Metrik-Analyse
Vergleiche in Langfuse alle drei Konfigurationen:
1. Baseline (small embedding + gpt-4.1-nano)
2. Large embedding + gpt-4.1-nano
3. Large embedding + gpt-5

### Reflexionsfragen
1. Welche Konfiguration liefert die besten Ergebnisse?
2. Rechtfertigt die Qualitätsverbesserung die höheren Kosten?
3. Gibt es Metriken, die sich verschlechtert haben? Warum?
4. Für welche Use Cases würdest du welche Konfiguration empfehlen?

## Erweiterte Aufgaben (Optional)
- Teste weitere Embedding-Modelle (z.B. `text-embedding-ada-002`)
- Teste weitere Chat-Modelle (z.B. `gpt-4.1-mini`, `gpt-4.1`, `gpt-5-nano`, `gpt-5-mini`)
