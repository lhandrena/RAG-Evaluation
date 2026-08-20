# 🚀 Advanced RAG Training

> Full-Stack RAG-Anwendung mit Frontend, Backend und Monitoring sowie isolierte Jupyter-Notebook-Übungen

## 📋 Inhaltsverzeichnis

- [Architektur-Übersicht](#-architektur-übersicht)
- [Voraussetzungen](#-voraussetzungen)
- [Setup (Ersteinrichtung)](#-setup-ersteinrichtung)
- [Schnellstart](#-schnellstart)
- [RAG-Optimierungs-Challenge (Aufgabe 5)](#-rag-optimierungs-challenge-aufgabe-5)
- [Alternative: Langfuse Cloud](#-alternative-langfuse-cloud)
- [Projektstruktur](#-projektstruktur)
- [Plattform-spezifische Hinweise](#-plattform-spezifische-hinweise)
- [Troubleshooting](#-troubleshooting)

---

## 🏗️ Architektur-Übersicht

```
┌─────────────────────────────────────────────────┐
│  Docker  (docker compose)                       │
│  ┌─────────────┐ ┌──────────┐ ┌──────────────┐  │
│  │  Langfuse   │ │ Frontend │ │    Neo4j     │  │
│  │  :3000      │ │ :5173    │ │  :7474/:7687 │  │
│  └─────────────┘ └──────────┘ └──────────────┘  │
└─────────────────────────────────────────────────┘
                       ▲
                       │ REST API (:5000)
                       │
              ┌────────┴────────┐
              │  Backend (lokal)│
              │  Python / uv    │
              └─────────────────┘
```

**Bevorzugter Weg:** Langfuse, Frontend und Neo4j laufen via Docker Compose – das Backend läuft lokal mit Python/uv.

> **Alternative:** Statt Langfuse lokal im Docker zu betreiben, kann auch eine [Langfuse Cloud](https://cloud.langfuse.com)-Instanz genutzt werden. Das Frontend kann in diesem Fall ebenfalls lokal (ohne Docker) gestartet werden. Siehe [Alternative: Langfuse Cloud](#-alternative-langfuse-cloud).

---

## ✅ Voraussetzungen

| Tool | Zweck |
|------|-------|
| **Docker** | Langfuse, Frontend, Neo4j als Container |
| **Python 3.12** | Backend-Runtime |
| **uv** | Python Package Manager (schneller pip-Ersatz) |
| **OpenAI API Key** | LLM-Zugriff für RAG-Pipeline & Evaluation |

---

## 🛠️ Setup (Ersteinrichtung)

### 1️⃣ Environment-Variablen

```bash
cp .env.example .env
```

In `.env` eintragen:
- `OPENAI_API_KEY` – wird im Kurs zur Verfügung gestellt (oder eigener Key)

> Die Langfuse-Keys (`LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`) werden in Schritt 3 ergänzt.

### 2️⃣ Docker-Services starten (Langfuse, Frontend, Neo4j)

```bash
docker compose --env-file .env \
  -f infrastructure/langfuse_frontend_local.yml \
  -f infrastructure/neo4j.yml \
  up -d
```

### 3️⃣ Langfuse konfigurieren

1. Browser öffnen: http://localhost:3000
2. Benutzer anlegen
3. Organisation anlegen
4. Projekt erstellen
5. **Settings → API Keys** → Keys generieren (Public + Secret Key)
6. Generierte Keys in `.env` eintragen:
   ```
   LANGFUSE_PUBLIC_KEY=pk-lf-...
   LANGFUSE_SECRET_KEY=sk-lf-...
   ```

### 4️⃣ Python-Umgebung einrichten

<details>
<summary><b>uv installieren (falls noch nicht vorhanden)</b></summary>

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
# Python installieren (falls nicht vorhanden)
uv python install

# Dependencies installieren
uv sync
```

### 5️⃣ Backend starten

```bash
uv run --env-file .env python -m advanced_rag.backend.main
```

<details>
<summary><b>Alternative Startmöglichkeiten (VSCode)</b></summary>

- **Run Config:** `backend`
- **Debug:** `debug backend` in der Command Palette

</details>

### ✅ Funktionstest

1. Frontend öffnen: http://localhost:5173
2. Frage stellen: *„Wer ist Bundeskanzler?"* (erste Anfrage dauert länger)
3. Antwort sollte erscheinen
4. Langfuse prüfen: http://localhost:3000 → **Tracing** → Traces sichtbar

**Zugriff auf alle Services:**

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Langfuse (Monitoring) | http://localhost:3000 |
| Neo4j Browser | http://localhost:7474 |

<details>
<summary><b>⏱️ Warum dauert die erste Anfrage länger?</b></summary>

Bei der ersten Nachricht werden folgende Komponenten initialisiert:

1. **Dokumente laden** – Alle Dateien aus dem konfigurierten Quellverzeichnis werden eingelesen
2. **Chunking** – Dokumente werden in kleinere Abschnitte aufgeteilt
3. **Embeddings generieren** – Für jeden Chunk wird ein Vektor-Embedding erstellt
4. **Vektordatenbank aufbauen** – Chroma-Datenbank wird mit den Embeddings befüllt
5. **LangGraph kompilieren** – Retrieval-Pipeline wird aufgebaut (Retriever → Reranker → Generator)

**Lazy Loading:** Die Initialisierung erfolgt erst beim ersten Request, nicht beim Backend-Start. Nachfolgende Anfragen sind deutlich schneller.

</details>

---

## ⚡ Schnellstart

> Nur für den Fall, dass das Projekt **bereits einmal vollständig eingerichtet** wurde.

```bash
# 1. Docker-Services starten
docker compose --env-file .env \
  -f infrastructure/langfuse_frontend_local.yml \
  -f infrastructure/neo4j.yml \
  up -d

# 2. Backend starten
uv run --env-file .env python -m advanced_rag.backend.main
```

---

## 🏁 RAG-Optimierungs-Challenge (Aufgabe 5)

Die Abschluss-Challenge ([`aufgaben/5_RAG_RAG.md`](aufgaben/5_RAG_RAG.md)) startet von einem vorbereiteten Branch, damit alle vom gleichen Punkt loslegen:

```bash
git fetch && git checkout rag-challenge
```

Der Branch enthält den gemeinsamen Startpunkt (vorkonfigurierte Skripte, Metriken und ein Agenten-Leitfaden `AGENTS.md`) — alle Details stehen in der Aufgabe auf dem Branch.

---

## ☁️ Alternative: Langfuse Cloud

Statt Langfuse lokal im Docker zu betreiben, kann eine **Langfuse Cloud**-Instanz unter [cloud.langfuse.com](https://cloud.langfuse.com) verwendet werden.

**Anpassungen in `.env`:**
```
LANGFUSE_HOST=https://cloud.langfuse.com
LANGFUSE_PUBLIC_KEY=pk-lf-...   # aus Langfuse Cloud Dashboard
LANGFUSE_SECRET_KEY=sk-lf-...   # aus Langfuse Cloud Dashboard
```

**Frontend lokal starten (ohne Docker):**
```bash
cd frontend
npm install
npm run dev
```

**Docker-Befehl ohne Langfuse (nur Neo4j):**
```bash
docker compose --env-file .env -f infrastructure/neo4j.yml up -d
```

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
- `debug backend` – Backend mit Debugger starten
- `debug evaluation` – Evaluation-Skripte debuggen

</details>

---

## 📚 Weitere Ressourcen

- **Backend-Details:** [`src/advanced_rag/backend/README.md`](src/advanced_rag/backend/README.md)
- **Evaluation-Guide:** [`src/advanced_rag/evaluation/README.md`](src/advanced_rag/evaluation/README.md)
- **Scraping-Docs:** [`src/advanced_rag/scraping/README.md`](src/advanced_rag/scraping/README.md)
- **Übungsaufgaben:** [`aufgaben/`](aufgaben/)

---

## 🔧 Troubleshooting

<details>
<summary><b>Port-Konflikt: Langfuse-Port 3000 ist bereits belegt</b></summary>

Falls Port `3000` auf dem Host bereits von einer anderen Anwendung verwendet wird (z. B. ein anderer Webserver oder React Dev-Server), kann der Langfuse-Port wie folgt geändert werden – z. B. auf `3001`:

**1. Port-Mapping in Docker Compose anpassen**

In `infrastructure/langfuse_frontend_local.yml` den Port des `langfuse-web`-Services ändern:

```yaml
langfuse-web:
  ports:
    - "3001:3000"   # Host-Port 3001 → Container-Port 3000
  environment:
    NEXTAUTH_URL: http://localhost:3001   # muss zum neuen Host-Port passen
```

**2. `LANGFUSE_HOST` in `.env` aktualisieren**

```
LANGFUSE_HOST="http://localhost:3001"
```

**3. Docker-Services neu starten**

Langfuse ist danach unter http://localhost:3001 erreichbar.

</details>

<details>
<summary><b>Port-Konflikte anderer Services</b></summary>

Das Projekt verwendet mehrere Ports. Falls ein Port bereits belegt ist, kann jeweils der **Host-Port** (linke Seite) im entsprechenden Docker-Compose-File angepasst werden:

| Service | Standard-Port | Datei |
|---------|--------------|-------|
| Langfuse Web | `3000` | `infrastructure/langfuse_frontend_local.yml` |
| Langfuse Worker | `3030` | `infrastructure/langfuse_frontend_local.yml` |
| Frontend | `5173` | `infrastructure/langfuse_frontend_local.yml` |
| PostgreSQL | `5432` | `infrastructure/langfuse_frontend_local.yml` |
| Redis | `6379` | `infrastructure/langfuse_frontend_local.yml` |
| ClickHouse HTTP | `8123` | `infrastructure/langfuse_frontend_local.yml` |
| ClickHouse Native | `9023` | `infrastructure/langfuse_frontend_local.yml` |
| MinIO API | `9090` | `infrastructure/langfuse_frontend_local.yml` |
| MinIO Console | `9092` | `infrastructure/langfuse_frontend_local.yml` |
| Neo4j Browser | `7474` | `infrastructure/neo4j.yml` |
| Neo4j Bolt | `7687` | `infrastructure/neo4j.yml` |

**Tipp:** Nur der Host-Port (links vom `:`) muss geändert werden. Der Container-Port (rechts) bleibt unverändert.

Beispiel: PostgreSQL von `5432` auf `5433` ändern:
```yaml
ports:
  - "5433:5432"
```

</details>
