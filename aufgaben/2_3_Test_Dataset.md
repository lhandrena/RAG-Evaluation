# Aufgabe 2.3: Test Dataset

## Lernziele
- Verstehen der Bedeutung qualitativ hochwertiger Test-Datensätze für RAG-Evaluation
- Kriterien für gute Frage-Antwort-Paare kennenlernen
- KI-generierte Datensätze kritisch bewerten können

## Voraussetzungen
keine

## Teil 1: Manuellen Datensatz erstellen (10 Minuten)

Erstelle einen Datensatz aus Fragen und erwarteten Antworten (Ground Truth) zu einem Kurzartikel in diesem Ordner: [`../src/advanced_rag/evaluation/datasets/openai_article/`](../src/advanced_rag/evaluation/datasets/openai_article/)

- lese den Artikel openai_article.pdf
- befülle `dataset_for_openai_article.csv` mit Fragen-Antwort-Paaren.

Mache dir dabei folgende Gedanken:

1. Welche handfesten Informationen stecken in diesem Dokument?
2. Was für unterschiedliche Personas könnten Fragen zum Thema Fine Tuning stellen?
3. Wie würden unterschiedliche Personas Fragen stellen? Welche Begriffe/Synonyme würden sie verwenden?

Nutze ein LLM deiner Wahl, um eine möglichst große Variation an Formulierungen zu generieren.


## Teil 2: KI-generierte Datensätze bewerten (10 Minuten)

Schaue dir stichprobenartig die Tagesschau-Artikel in [`src/advanced_rag/scraping/tagesschau_dump/`](../src/advanced_rag/scraping/tagesschau_dump/) an.

Öffne mehrere Datensätze in [`src/advanced_rag/evaluation/datasets/tagesschau/`](../src/advanced_rag/evaluation/datasets/tagesschau/) und bewerte sie nach folgenden Kriterien:

**Bewertungskriterien:**
- ✅ Sind die Fragen realistisch?
- ✅ Sind die Fragen alleinstehend sinnvoll?
- ✅ Sind die Antworten korrekt und vollständig?
- ⚠️ Sind die Fragen zu einfach/zu komplex?

### Reflexionsfragen
1. Was sind die Vor- und Nachteile KI-generierter Datensätze?
2. Wann sollte man manuelle vs. automatische Datensatz-Erstellung bevorzugen?
3. Wie viele Fragen braucht man für eine aussagekräftige Evaluation?

## Wichtige Erkenntnisse
- 📊 **Qualität vor Quantität:** Wenige gute Fragen sind besser als viele schlechte
- 🎯 **Realitätsnähe:** Fragen sollten echte User-Anfragen widerspiegeln
- 🔄 **Diversität:** Verschiedene Fragetypen und Schwierigkeitsgrade sind wichtig
- ⚖️ **Balance:** Mix aus manuellen und KI-generierten Fragen oft optimal