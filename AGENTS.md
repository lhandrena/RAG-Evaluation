# Agenten-Leitfaden: RAG-Optimierungs-Challenge

Dieses Repo ist eine RAG-Trainingsanwendung (LangGraph-Backend, Chroma-Vektordatenbank, Langfuse-Evaluation). Auf dem Branch `rag-challenge` sollen die Retrieval- und Generierungsqualität der Anwendung iterativ verbessert werden. Der Mensch ist Navigator (Anforderungen, Hypothesen, Bewertung) — du als KI-Agent setzt Änderungen um.

## Spielregeln (wichtig!)

Die Evaluation ist der Schiedsrichter der Challenge und darf nicht manipuliert werden:

- **Tabu:** Änderungen an `src/advanced_rag/evaluation/**` (Metriken, Eval-Skripte, Datensätze) und an den Quelldokumenten in `src/advanced_rag/scraping/**`.
- **Tabu:** Quellen-Dateinamen oder erwartete Antworten aus dem Datensatz in Prompts oder Code hardcoden.
- **Erlaubt:** Alles an der RAG-Pipeline selbst — Chunking, Retrieval, Reranking, Prompts, Modelle, Konfiguration in `.env`.
- Pro Iteration möglichst nur einen Hauptfaktor ändern, damit Ursache und Wirkung nachvollziehbar bleiben.

## Anwendung starten & evaluieren

```bash
# Backend (muss nach Konfig-Änderungen neu gestartet werden)
uv run --env-file .env python -m advanced_rag.backend.main

# Evaluations-Dataset nach Langfuse hochladen (einmalig)
uv run --env-file .env python src/advanced_rag/evaluation/upload_datasets.py

# Evaluation ausführen (Backend muss laufen)
uv run --env-file .env python src/advanced_rag/evaluation/evaluate_dataset.py
```

Ergebnisse erscheinen in Langfuse (http://localhost:3000) unter **Datasets → rag_source**. Der Experiment-Name kodiert die Konfiguration (Chunking, Retriever, Reranking), siehe `assemble_experiment_name_from_env()` in `evaluate_dataset.py`.

**Ziel-Metriken der Challenge:** `context_sources_f1` und `faithfulness`.

## Stellschrauben

### Konfiguration in `.env` (Backend-Neustart nötig)

| Variable | Werte / Bedeutung |
|---|---|
| `CHUNKING_STRATEGY` | `RECURSIVE`, `SEMANTIC`, `SEMANTIC_LLM` |
| `CHUNK_SIZE` / `CHUNK_OVERLAP` | Zeichen pro Chunk / Überlappung (nur `RECURSIVE`) |
| `RETRIEVER_TYPE` | `SIMILARITY_SEARCH`, `HYBRID_SEARCH`, `QUERY_EXPANSION`, `QUERY_EXPANSION_LC` |
| `RETRIEVED_NUMBER_OF_DOCUMENTS` | Anzahl abgerufener Chunks (k) |
| `USE_RERANKING` | `True`/`False` — Cross-Encoder-Reranking |
| `CONTEXT_SIZE_AFTER_RERANKING` | Chunks, die das Reranking überleben |
| `CHAT_MODEL` / `EMBEDDING_MODEL` | OpenAI-Modelle für Generierung / Embeddings |
| `AVG_CHUNK_SIZE`, `BREAKPOINT_PERCENTILE_THRESHOLD`, `BUFFER_SIZE` | Parameter für `SEMANTIC` Chunking |
| `MAX_CHUNK_TOKEN` | Parameter für `SEMANTIC_LLM` Chunking |

`DOCUMENT_SOURCE` bleibt auf `SCRAPED_DATA` — die Datenquelle ist Teil der Challenge-Definition.

### Code-Switches

- **Generierungs-Prompt:** `src/advanced_rag/backend/nodes/prompt_templates/` — aktive Datei wird in `augmented_generation_prompt.py` gewählt; Prompt-Texte liegen in `generation_prompt_good.txt` / `generation_prompt_bad.txt` (eigene Varianten sind erlaubt).
- **Retriever-Implementierungen:** `src/advanced_rag/backend/nodes/` (`similarity_retriever.py`, `hybrid_retriever.py`, `query_expansion_retriever.py`, `reranker.py`).
- **Pipeline-Aufbau:** `src/advanced_rag/backend/core/application.py` (`build_graph`, `create_retriever`).

## Vektordatenbank-Verhalten (spart Zeit)

- Chroma persistiert nach `./chroma_langchain_db_<CHUNK_SIZE>_<CHUNK_OVERLAP>`; die Collection heißt `<DOCUMENT_SOURCE>_<CHUNKING_STRATEGY>`.
- Änderung von `CHUNK_SIZE`/`CHUNK_OVERLAP`/`CHUNKING_STRATEGY`/`DOCUMENT_SOURCE` ⇒ neue Collection bzw. neues Verzeichnis, wird beim Backend-Start automatisch neu indexiert. **Kein manuelles Löschen nötig.**
- Änderung von `EMBEDDING_MODEL` ⇒ Verzeichnis/Collection-Name ändern sich NICHT ⇒ vorher `rm -rf chroma_langchain_db_*`, sonst mischen sich alte und neue Embeddings.
- Reine Retriever-/Reranking-/Prompt-/Chat-Modell-Änderungen brauchen nur einen Backend-Neustart, kein Re-Indexing.
