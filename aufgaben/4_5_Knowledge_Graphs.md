# Aufgabe 4.5: Knowledge Graphs mit Neo4j

## Lernziele
- Verstehen, wie Knowledge Graphs in RAG-Systemen funktionieren
- Umstellung von Vektor-basiertem Retrieval auf Graph-basiertes Retrieval
- Neo4j Frontend nutzen, um Knowledge Graphs zu visualisieren
- Analysieren, wie Entitäten und Beziehungen im Graph strukturiert sind
- Vergleich: Vector Search vs. Knowledge Graph Retrieval

## Was ist ein Knowledge Graph?

Ein **Knowledge Graph** ist eine strukturierte Repräsentation von Wissen als Netzwerk von Entitäten und ihren Beziehungen:

- **Entitäten (Nodes)**: Personen, Orte, Konzepte, Objekte
- **Beziehungen (Edges)**: Verbindungen zwischen Entitäten ("arbeitet_für", "ist_verwandt_mit", "befindet_sich_in")
- **Eigenschaften**: Zusätzliche Informationen zu Entitäten und Beziehungen

### Beispiel: Shakespeare-WissensGraph

```
[Romeo] ---(IST_CHARAKTER_IN)---> [Romeo und Julia]
   |
   |---(LIEBT)---> [Julia]
   |
   |---(IST_MITGLIED_VON)---> [Montague Familie]

[Julia] ---(IST_MITGLIED_VON)---> [Capulet Familie]
   |
   |---(LIEBT)---> [Romeo]
```

### Warum Knowledge Graphs für RAG?

**Vorteile gegenüber reiner Vektor-Suche:**
- ✅ **Strukturierte Beziehungen**: Erfasst explizite Verbindungen zwischen Konzepten
- ✅ **Traversierung**: Kann über mehrere Hops relevante Informationen finden
- ✅ **Kontextuelles Verständnis**: Versteht Zusammenhänge, nicht nur semantische Ähnlichkeit
- ✅ **Erklärbarkeit**: Zeigt den Pfad, wie Informationen gefunden wurden

**Beispiel:**
- **Vector Search Query**: "Wer liebt wen in Romeo und Julia?"
  - Findet Textpassagen über "Liebe" und "Romeo und Julia"
  - Versteht Beziehungen nur implizit aus Text

- **Knowledge Graph Query**: "Wer liebt wen in Romeo und Julia?"
  - Traversiert explizite LIEBT-Beziehungen im Graph
  - Kann komplexe Beziehungsketten folgen (Romeo → liebt → Julia → ist_Mitglied_von → Capulet Familie)
  - Liefert strukturierte, präzise Antworten

## Teil 1: Von Application zu GraphApplication

Die RAG-Anwendung unterstützt zwei Retrieval-Methoden:
1. **Application**: Vector-basiertes Retrieval mit ChromaDB
2. **GraphApplication**: Knowledge Graph Retrieval mit Neo4j

### Schritt 1: Code-Änderung in main.py

Öffne die Datei [`src/advanced_rag/backend/main.py`](../src/advanced_rag/backend/main.py) und mache folgende Änderungen:

**VORHER: Vector-basiertes Retrieval**
```python
from advanced_rag.backend.core.application import Application

# ...

def create_flask_app():
    langfuse_handler = CallbackHandler()

    logging.info("Initializing application core...")
    app_core = Application(langfuse_handler)

    logging.info("Warming up application...")
    _ = app_core.vector_store
    _ = app_core.graph
    logging.info("Application ready!")
```

**NACHHER: Knowledge Graph Retrieval**
```python
from advanced_rag.backend.core.graph_application import GraphApplication

# ...

def create_flask_app():
    langfuse_handler = CallbackHandler()

    logging.info("Initializing application core...")
    app_core = GraphApplication(langfuse_handler)

    logging.info("Warming up application...")
    _ = app_core.build_graph()
    logging.info("Application ready!")
```

### Was passiert hier?

**GraphApplication macht folgendes anders:**
1. **Lädt Dokumente**: Shakespeare-Texte werden aus dem `documents/shakespeare_dump` Ordner geladen
2. **Chunking**: Dokumente werden in kleinere Abschnitte aufgeteilt (empfohlene Chunk Size=6000,Overlap=3000)
3. **Summarization**: Jeder Chunk wird vom LLM zusammengefasst, um wichtige Entitäten zu extrahieren
4. **Graph-Transformation**: LLM extrahiert Entitäten und Beziehungen aus den Chunks
5. **Speicherung in Neo4j**: Graph wird in der Neo4j-Datenbank gespeichert

**Code-Flow (siehe [`graph_document_processor.py`](../src/advanced_rag/backend/services/graph_document_processor.py)):**
```
Dokumente laden → Chunking → Summarization → Graph-Extraktion → Neo4j
```

### Schritt 2: Neo4j starten

Neo4j muss laufen, damit die Anwendung funktioniert. Starte Neo4j mit Docker Compose:

```bash
# Starte Neo4j
docker compose -f infrastructure/neo4j.yml up -d
```

**Was macht dieser Befehl?**
- Startet einen Neo4j Container
- Ports 7474 (Browser) und 7687 (Bolt-Protokoll) werden exponiert
- Login-Credentials: `neo4j` / `password`
- Daten werden persistent in `./neo4j/data` gespeichert

**Verbindungsdetails (bereits in `.env` konfiguriert):**
```env
NEO4J_URI=bolt://127.0.0.1:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password
```

### Schritt 3: Backend starten

Starte das Backend neu, damit die Änderungen wirksam werden:

```bash
uv run --env-file .env python -m src.advanced_rag.backend.main
```

**Was passiert beim Start:**
- ✓ GraphApplication wird initialisiert
- ✓ Verbindung zu Neo4j wird hergestellt
- ✓ Falls die Datenbank leer ist: Knowledge Graph wird erstellt
- ✓ Dokumente werden geladen, gechunkt, und in Graph-Struktur konvertiert
- ⏳ **Achtung**: Erste Ausführung kann 2-5 Minuten dauern (LLM muss jeden Chunk analysieren)!

**Erwartete Log-Ausgaben:**
```
🚀 Starting backend, loading dependencies...
Initializing application core...
Loading documents from shakespeare_dump...
Splitting documents into chunks...
number of chunks: 150
Converting to graph documents...
Time taken to convert to graph documents: 180 seconds
Warming up application...
Application ready!
```

## Teil 2: Knowledge Graph im Neo4j Frontend visualisieren

Neo4j bietet ein Browser-Interface, um den Knowledge Graph zu erkunden.

### Neo4j Browser öffnen und erkunden

Öffne den Neo4j Browser in deinem Webbrowser:
```
http://localhost:7474
```

**Login:**
- **Username**: neo4j
- **Password**: password

### Erkunde den Graph

Klicke dich durch den Knowledge Graph und erkunde die Struktur:
- Verschiedene **Nodes** (Kreise/Punkte) repräsentieren Entitäten (Charaktere, Orte, Konzepte)
- **Edges** (Linien) zwischen Nodes zeigen Beziehungen (liebt, ist_Mitglied_von, etc.)

**Aufgabe:** Klicke einzelne Nodes an, erkunde ihre Verbindungen und versuche zu verstehen:
- Welche Arten von Entitäten gibt es?
- Wie sind die Charaktere miteinander verbunden?
- Welche Beziehungstypen existieren?

## Teil 3: Fragen an die Graph-basierte RAG-Anwendung stellen

Jetzt, wo der Knowledge Graph aktiv ist, kannst du Fragen stellen.

### Schritt 1: Frontend öffnen

Öffne das Frontend:
```
http://localhost:5173
```

### Schritt 2: Decke ein Komplott auf
- Frage "Who's planning a murder?"
- Folgefrage "Who is the target?"

Hier kann es passieren, dass das Backend einen Fehler wirft. Mit ein wenig Prompt Engineering können wir diesen allerdings beheben. Den Prompt zum Erstellen von Queries findest du hier: `src/advanced_rag/backend/nodes/prompt_templates/cypher_generation_prompt.py`

### Neo4j-Datenbank zurücksetzen

Falls du den Graph neu aufbauen möchtest:

```cypher
# Im Neo4j Browser: Lösche alle Nodes und Beziehungen
MATCH (n)
DETACH DELETE n
```

Beim nächsten Backend-Start wird der Graph neu erstellt.

## Reflexionsfragen

1. **Wann ist Knowledge Graph Retrieval besser als Vector Search?**
   - Bei Fragen über Beziehungen und Strukturen
   - Wenn explizite Verbindungen wichtig sind
   - Bei komplexen, mehrschichtigen Queries

2. **Wann ist Vector Search besser?**
   - Bei semantischer Ähnlichkeit ohne klare Struktur
   - Bei unstrukturierten Texten
   - Wenn Beziehungen implizit im Text sind

3. **Hybrid-Ansatz: Wann beide kombinieren?**
   - Vector Search für breiten Recall
   - Knowledge Graph für präzise Beziehungen
   - Best of both worlds!

## Zusammenfassung

### Was hast du gelernt?

1. **Knowledge Graphs strukturieren Wissen explizit:**
   - Entitäten und Beziehungen werden modelliert
   - Traversierung über mehrere Hops möglich
   - Erklärbare, präzise Antworten

2. **GraphApplication nutzt Neo4j:**
   - Dokumente werden in Graph-Struktur konvertiert
   - LLM extrahiert Entitäten und Beziehungen
   - Cypher-Queries durchsuchen den Graph

3. **Neo4j Browser ermöglicht Exploration:**
   - Visualisierung des Knowledge Graphs
   - Cypher-Queries für Ad-hoc-Analysen
   - Verständnis der Graph-Struktur

4. **Trade-offs beachten:**
   - ✅ Präzise bei strukturierten Fragen
   - ✅ Explizite Beziehungen
   - ❌ Längere Verarbeitungszeit (Graph-Erstellung)
   - ❌ Komplexität bei unstrukturierten Fragen

