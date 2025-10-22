# 🚀 Advanced RAG Training

> Full-Stack RAG-Anwendung mit Frontend, Backend und Monitoring sowie isolierte Jupyter-Notebook-Übungen

## 📋 Inhaltsverzeichnis

- [Schnellstart](#-schnellstart)
- [Projektstruktur](#-projektstruktur)
- [Setup](#-setup)
- [Plattform-spezifische Hinweise](#-plattform-spezifische-hinweise)

---

## ⚡ Schnellstart
Beim ersten Einrichten folge den Schritten in [Setup](#-setup).
```bash
# 1. Services starten (Langfuse, Neo4j, Frontend)
docker compose -f infrastructure/langfuse_local.yml -f infrastructure/neo4j.yml up -d

# 2. Python-Umgebung einrichten
uv sync

# 3. Environment-Variablen konfigurieren
cp .env.example .env
# → Langfuse Keys und OpenAI API Key in .env eintragen

# 4. Backend starten
uv run --env-file .env python -m advanced_rag.backend.main
```

**Zugriff:**
- Frontend: http://localhost:5173
- Langfuse (Monitoring): http://localhost:3000
- Neo4j Browser: http://localhost:7474

---

## 📁 Projektstruktur

```
src/advanced_rag/
├── backend/             # RAG-Backend mit LangGraph
│   ├── core/            # Application & GraphApplication
│   ├── nodes/           # Retriever, Reranker, Generator
│   ├── services/        # DocumentProcessor, Chunker
│   └── main.py          # Backend-Einstiegspunkt
│
├── evaluation/          # Metriken & Testdaten
│   ├── metrics/         # RAGAS & Custom Metrics
│   ├── datasets/        # Evaluierungs-Datasets
│   └── testset/         # Testset-Generierung
│
└── scraping/            # Datenquellen
    ├── tagesschau_dump/ # Deutsche Nachrichtenartikel
    ├── llm_paper/       # Forschungspapiere
    └── knowledge_graph/ # Graph-Beispieldaten

frontend/                # React/TypeScript UI
infrastructure/          # Docker-Compose Configs
aufgaben/                # Übungsaufgaben
```

<details>
<summary><b>📦 Komponenten-Details</b></summary>

### Backend
- **LangGraph-basierte RAG-Pipeline** mit verschiedenen Retrieval-Strategien
- **Retrieval-Modi:** Similarity, Hybrid, Query Expansion
- **Knowledge Graph Integration** mit Neo4j
- **FastAPI REST-API** für Frontend-Kommunikation

### Evaluation
- **RAGAS-Metriken** für RAG-Qualitätsbewertung
- **Synthetische Testdaten-Generierung**
- **Langfuse-Integration** für LLM Observability
- **Vorgefertigte Datasets** (Tagesschau, LLM-Papers)

### Frontend
- **React + TypeScript** Chat-Interface
- **Docker-Container** für einfaches Deployment
- **REST-API Integration** mit Backend

### Infrastructure
- **Langfuse:** LLM Monitoring & Tracing
- **Neo4j:** Knowledge Graph Storage
- **Docker Compose:** One-Command Setup

</details>

---

## 🛠️ Setup

### 1️⃣ Langfuse und Frontend starten

```bash
# Docker Compose starten
docker compose -f infrastructure/langfuse_local.yml -f infrastructure/neo4j.yml up -d
```

**Langfuse konfigurieren:**
1. Browser öffnen: http://localhost:3000
2. Benutzer anlegen
3. Projekt erstellen
4. In Langfuse unten rechts auf Settings → API Keys → API Keys generieren (Public + Secret Key)

### 2️⃣ Environment-Variablen

```bash
# .env-Datei erstellen
cp .env.example .env
```

In `.env` eintragen:
- `LANGFUSE_PUBLIC_KEY` und `LANGFUSE_SECRET_KEY` (aus Langfuse UI)
- `OPENAI_API_KEY` (OpenAI API Key)

### 3️⃣ Python-Umgebung

<details>
<summary><b>uv installieren</b></summary>

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (pip):**
```bash
pip install uv
```

</details>

```bash
# Python 3.12.9 installieren (falls nicht vorhanden)
uv python install

# Dependencies installieren
uv sync
```

### 4️⃣ Backend starten

```bash
# Run Config: `backend`
# oder in VSCode Run Config: `debug backend` in der Command Palette
# oder via Terminal:
uv run --env-file .env python src/advanced_rag/backend/main.py


```

### ✅ Funktionstest

1. Frontend öffnen: http://localhost:5173
2. Frage: Wer ist Bundeskanzler? (dauert länger - siehe unten)
3. Antwort sollte erscheinen
4. Langfuse prüfen: http://localhost:3000 → Traces sichtbar, verwendeter Kontext sichtbar

<details>
<summary><b>⏱️ Warum dauert die erste Anfrage länger?</b></summary>

Bei der ersten Nachricht werden folgende Komponenten initialisiert:

1. **Dokumente laden** - Alle Dateien aus dem konfigurierten Quellverzeichnis werden eingelesen
2. **Chunking** - Dokumente werden in kleinere Abschnitte aufgeteilt (Recursive/Semantic/LLM-basiert)
3. **Embeddings generieren** - Für jeden Chunk wird ein Vektor-Embedding erstellt
4. **Vektordatenbank aufbauen** - Chroma-Datenbank wird mit den Embeddings befüllt
5. **LangGraph kompilieren** - Retrieval-Pipeline wird aufgebaut (Retriever → Reranker → Generator)

**Lazy Loading:** Diese Initialisierung erfolgt erst beim ersten Request, nicht beim Backend-Start. Nachfolgende Anfragen nutzen die bereits aufgebaute Infrastruktur und sind deutlich schneller.

</details>

---

## 🖥️ Plattform-spezifische Hinweise

<details>
<summary><b>macOS</b></summary>

### NLTK Dependencies

Manuelle Installation erforderlich ([NLTK Docs](https://www.nltk.org/data.html#manual-installation)):

1. **Ordner erstellen:**
   ```bash
   mkdir -p ~/nltk_data/taggers ~/nltk_data/tokenizers
   ```

2. **Dependencies herunterladen:**
   - [averaged_perceptron_tagger_eng](https://www.nltk.org/nltk_data/)
   - [punkt_tab](https://www.nltk.org/nltk_data/)

3. **In entsprechende Ordner ablegen:**
   - `averaged_perceptron_tagger_eng` → `~/nltk_data/taggers/`
   - `punkt_tab` → `~/nltk_data/tokenizers/`

</details>

<details>
<summary><b>VSCode Run Configurations</b></summary>

Verfügbare Configs in der Command Palette:
- `debug backend` - Backend mit Debugger starten
- `debug evaluation` - Evaluation-Skripte debuggen

</details>

---

## 📚 Weitere Ressourcen

- **Backend-Details:** [`src/advanced_rag/backend/README.md`](src/advanced_rag/backend/README.md)
- **Evaluation-Guide:** [`src/advanced_rag/evaluation/README.md`](src/advanced_rag/evaluation/README.md)
- **Scraping-Docs:** [`src/advanced_rag/scraping/README.md`](src/advanced_rag/scraping/README.md)
- **Übungsaufgaben:** [`aufgaben/`](aufgaben/)
