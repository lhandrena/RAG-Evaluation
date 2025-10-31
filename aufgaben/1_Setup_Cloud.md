# Aufgabe 1: Setup

Richte die RAG-Anwendung für die Cloud-Instanz ein:

## Voraussetzungen

1. **Erstelle eine `.env` Datei** im Root-Verzeichnis:
   ```bash
   cp .env.example .env
   ```
   Füge dann deinen OpenAI API Key hinzu:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
2. **Richte Langfuse ein**:
   - Erstelle einen Account auf [cloud.langfuse.com](https://cloud.langfuse.com)
   - Lege eine neue Organisation an
   - Erstelle ein neues Projekt
   - Kopiere die API Keys in die `.env` Datei


3. **Starte das Frontend**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
4. **Starte das Backend**:

   Ab hier kannst du dem [README](../README.md#3-backend-starten) ab Schritt 3 folgen.

## Chatte mit der Anwendung

Nachdem das Setup abgeschlossen ist, chatte über das Frontend (http://localhost:5173) mit der RAG-Anwendung.

**Ziel:** Ein Gefühl für das System bekommen - wie verhält es sich?

### Optional: Experimentiere mit verschiedenen Fragen

- Stelle normale Fragen zu den Dokumenten
- Versuche Prompt-Hacking (z.B. "Ignoriere alle vorherigen Anweisungen und...")
- Versuche Halluzinationen zu produzieren (Fragen zu Themen, die nicht in den Dokumenten sind)
- Versuche das System zu Falschaussagen zu bewegen
- Teste Edge-Cases und ungewöhnliche Anfragen

