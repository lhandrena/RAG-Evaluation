# RAG Anwendungen evaluieren

## Setup

Um mit der Evaluation zu beginnen, muss zunächst die Datei `.env.example` kopiert und in `.env` umbenannt werden:

```bash
cp .env.example .env
```

In dieser Datei werden dann folgende Variablen eingetragen:
- `OPENAI_API_KEY` (OpenAI API Key)
- `LANGFUSE_PUBLIC_KEY` und `LANGFUSE_SECRET_KEY` (siehe unten)

### Services starten

Für die Evaluation unserer Anwendung verwenden wir Langfuse als Monitoring- und Evaluierungstool. Der erste Schritt besteht darin, die Container lokal zu starten:

```bash
docker compose -f infrastructure/langfuse_local.yml -f infrastructure/neo4j.yml up -d
```

**Langfuse konfigurieren:**

Nach dem erfolgreichen Start der Container öffnet man einen Browser und navigiert zu `http://localhost:3000`. Dort:

1. Benutzer anlegen
2. Projekt erstellen
3. API Keys generieren (Public + Secret Key)

Die generierten Keys müssen in die `.env`-Datei eingetragen werden:
- `LANGFUSE_SECRET_KEY=sk-...`
- `LANGFUSE_PUBLIC_KEY=pk-lf-...`

## Backend starten

### Python-Umgebung einrichten

Das Projekt verwendet `uv` als Package Manager. Falls noch nicht installiert, siehe [README.md](README.md#3️⃣-python-umgebung) für Installationsanweisungen.

```bash
# Dependencies installieren
uv sync
```

### Backend ausführen

Das Backend kann auf drei Arten gestartet werden:

```bash
uv run --env-file .env python -m advanced_rag.backend.main
```

## Frontend starten

Das Frontend wird über Docker Compose automatisch gestartet (siehe Services starten oben). Alternativ kann es manuell gestartet werden:

```bash
cd frontend
npm install
npm run dev
```

## Interaktion und Überprüfung

Nachdem sowohl Backend als auch Frontend erfolgreich gestartet wurden, kann man das Frontend im Browser aufrufen:

**Zugriff:**
- Frontend: http://localhost:5173
- Langfuse (Monitoring): http://localhost:3000
- Neo4j Browser: http://localhost:7474

Im Frontend stellt man eine Frage an die RAG-Anwendung. Um die Evaluation zu überprüfen, navigiert man zu Langfuse (http://localhost:3000) und überprüft die aufgezeichneten Traces, die detaillierte Informationen über die Verarbeitung der Anfrage enthalten.

**Hinweis:** Die erste Anfrage dauert länger, da die RAG-Pipeline initialisiert wird (Dokumente laden, Chunking, Embeddings generieren, Vektordatenbank aufbauen). Nachfolgende Anfragen sind deutlich schneller.
