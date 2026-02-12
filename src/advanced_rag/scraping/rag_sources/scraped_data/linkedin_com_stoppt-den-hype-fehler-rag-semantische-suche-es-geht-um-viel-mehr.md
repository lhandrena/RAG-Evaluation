# Source: https://www.linkedin.com/pulse/stoppt-den-hype-fehler-rag-semantische-suche-es-geht-um-biswanger-jvove
Number of words: 6587

# Stoppt den Hype-Fehler! RAG ≠ Semantische Suche. Es geht um viel mehr! 🚀

RAG: Das Entwurfsmuster für KI-gestützte UnternehmensdatenRetrieval-Augmented Generation (RAG) ist ein leistungsstarkes Entwurfsmuster für die KI-Entwicklung. Es erweitert Sprachmodelle mit unternehmensspezifischen Daten, ohne dass ein eigenes KI-Modell trainiert werden muss.Dabei kommt "indirekt" eine Technik namens „Few-Shot Learning“ aus dem Bereich des Prompt Engineerings zum Einsatz. Durch das Einbringen relevanter Informationen in den Prompt kann das Sprachmodell direkt auf diese zugreifen, wodurch die Wahrscheinlichkeit steigt, dass diese Daten zur Beantwortung genutzt werden. Dies reduziert Halluzinationen des Modells erheblich und die KI "kennt" eure Daten.Few-Shot Learning - Notwendige Informationen sind im Prompt enthaltenDer Trick hinter RAGDas Besondere an RAG ist, dass der Benutzerprompt im Hintergrund automatisch vom System erweitert wird -ohne dass der Nutzer dies bemerkt. Viele Artikel und Tutorials erklären dies anhand der Vektorisierung von Eingaben und deren Vergleich mit einer Vektordatenbank - ein Prozess, der als„Semantische Suche“bekannt ist. Falls du mehr über Vektordaten und semantische Suche erfahren möchtest, schau dir meine bisherigenLinkedIn-Postsan.Typische Illustration von RAG in Verbindung mit semantischer SucheDie Ursprünge von RAGIm Jahr 2020 veröffentlichtePatrick Lewismit seinem Team von Meta AI Research das Paper"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". Darin beschrieben sie das RAG-Modell, das vortrainierte Sprachmodelle mit einer externen Wissensbasis kombiniert. Diese Wissensbasis nutzteDense Passage Retrieval(DPR), wobei Wikipedia-Artikel als Vektorindex dienten.Patrick Lewis - Der RAG DaddyDas zentrale Ziel von RAG war jedoch nicht die Vektorsuche selbst, sondern die Nutzungexterner Wissensquellen, um die Genauigkeit und Aktualität generierter Texte zu verbessern. Die konkrete Implementierung durch DPR war nur eine von vielen möglichen Varianten.Herausforderungen der Semantischen SucheWarum wird semantische Suche oft in Verbindung mit RAG gebracht? Weil sie es ermöglicht, natürliche Sprache zu verstehen und nicht nur nach Keywords zu suchen. So wie wir es von Sprachmodellen lieben gelernt haben. Doch sie bringterhebliche Herausforderungenmit sich:Nur Ähnlichkeiten, keine exakten Treffer: Die Suche basiert auf Ähnlichkeiten - exakte Begriffe, nach denen gesucht wird, können in den Ergebnissen fehlen.Qualität der Embedding-Modelle: Die Leistungsfähigkeit der Modelle, die Texte in Vektoren umwandeln, bestimmt die Suchqualität - eine Optimierung ist aufwendig.Vektordatenbanken beeinflussen das Ergebnis stark: Jede Datenbank hat ihre eigenen Stärken und Schwächen, was die Relevanz der Ergebnisse ebenfalls beeinflusst.Lock-in-Effekt bei Embedding-Modellen: Ein Wechsel des Modells erfordert eine vollständige Neuerstellung der Vektorisierung aller Daten.Die Semantische Suche ist nicht per se schlecht - sie kann sinnvoll sein, für spezielle Anforderungen. Die größte Herausforderung besteht darin, dass ihre Funktionsweise an verschiedenen Stellen beeinflusst wird: Ist das Embedding-Modell unzureichend? Sind die Daten schlecht geschnitten (gechunkt)? Liegt es an der Vektordatenbank?Das Herausfinden der eigentlichen Fehlerquelle ist aufwändig und sehr schwer messbar.Für bestimmte Einsatzzwecke kann die semantische Suche hervorragend sein - insbesondere in Kombination mit einem Hybrid-Ansatz (Keyword- + semantische Suche).In vielen Fällen jedoch reicht eine traditionelle, klassische Suche völlig aus und vermeidet unnötige Komplexität.Was RAG wirklich bedeutetWie bereits erwähnt, geht es bei RAG lediglich darum,externe Datenquellen in die KI-Generierung einzubinden. Dies kann mit oder ohne semantische Suche erfolgen.Schon lange bevor RAG populär wurde, haben wir in unserer Twitch-Community„My Coding Zone“eine YouTube-Integration entwickelt. Dabei erzeugte der Prompt automatisch Keywords für eine YouTube-Suche und lieferte die Ergebnisse an das Modell zurück. Das Sprachmodell antwortete daraufhin, als hätte es direkten Zugriff auf alle unsere YouTube-Folgen.RAG mit YouTube-API + Keyword-SucheAuch in Unternehmen sind relevante Daten oft bereits verfügbar - nur nicht in „sexy“ Form. Doch das ist kein Problem: Eine klassische Datenbanksuche kann in vielen Fällen völlig ausreichen, um dem Modell relevante Informationen bereitzustellen.Möglichkeiten, RAG ohne Vektordatenbanken zu nutzen:Webseiten (Extranet/Intranet)Klassische DatenbanksuchenAPI-AbfragenDokumentenmanagement-SystemeCRM- oder ERP-SystemeLokale DateienFazitEs gibt unzählige „Hello World“-Tutorials zu RAG, die oft die semantische Suche als Standardlösung präsentieren. In kleinen Beispielen funktioniert das wunderbar, doch in der Realität bringt sie erhebliche Herausforderungen mit sich. Viele dieser Tutorials gehen nicht darauf ein, dass alternative Methoden oft praktikabler sind. Gerade in echten Projekten zeigt sich, dass klassische Suchansätze oder hybride Lösungen (Keyword- + semantische Suche) häufig effektiver sind als die reine semantische Suche.Meine Erfahrung aus Kundenprojekten zeigt, dass oft traditionelle Suchmethoden völlig ausreichen und viel Komplexität ersparen. Wo eine semantische Suche Sinn macht, haben wir sie gezielt in Hybrid-Ansätzen kombiniert - mit großem Erfolg.Wie sieht es bei euch aus? Nutzt ihr RAG mit oder ohne semantische Suche?Wenn ihr mit der semantischen Suche gearbeitet habt, seid ihr dabei ebenfalls auf eine meiner erwähnten Herausforderungen gestoßen?Ich bin gespannt auf eure Erfahrungen! 🚀LikeComment1715 CommentsGregor Biswanger✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer4moReport this commentJETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8ULikeReply1 ReactionRalf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentIch glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.LikeReply2 Reactions3 ReactionsRalf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentDu willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.LikeReply2 Reactions3 ReactionsLeonhard FischlLead Software Architect bei EXXETA AG8moReport this commentPhilipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?LikeReply1 Reaction2 ReactionsChristian HeyerKI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz8moReport this commentDas Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.LikeReply1 Reaction2 ReactionsSee more commentsTo view or add a comment,sign inMore articles by Gregor BiswangerThe Danger of MCP - What Every Developer Needs to Know 🚨Apr 17, 2025The Danger of MCP - What Every Developer Needs to Know 🚨It sounds like a smart solution. It promises efficiency and new possibilities.4610 Comments

RAG: Das Entwurfsmuster für KI-gestützte UnternehmensdatenRetrieval-Augmented Generation (RAG) ist ein leistungsstarkes Entwurfsmuster für die KI-Entwicklung. Es erweitert Sprachmodelle mit unternehmensspezifischen Daten, ohne dass ein eigenes KI-Modell trainiert werden muss.Dabei kommt "indirekt" eine Technik namens „Few-Shot Learning“ aus dem Bereich des Prompt Engineerings zum Einsatz. Durch das Einbringen relevanter Informationen in den Prompt kann das Sprachmodell direkt auf diese zugreifen, wodurch die Wahrscheinlichkeit steigt, dass diese Daten zur Beantwortung genutzt werden. Dies reduziert Halluzinationen des Modells erheblich und die KI "kennt" eure Daten.Few-Shot Learning - Notwendige Informationen sind im Prompt enthaltenDer Trick hinter RAGDas Besondere an RAG ist, dass der Benutzerprompt im Hintergrund automatisch vom System erweitert wird -ohne dass der Nutzer dies bemerkt. Viele Artikel und Tutorials erklären dies anhand der Vektorisierung von Eingaben und deren Vergleich mit einer Vektordatenbank - ein Prozess, der als„Semantische Suche“bekannt ist. Falls du mehr über Vektordaten und semantische Suche erfahren möchtest, schau dir meine bisherigenLinkedIn-Postsan.Typische Illustration von RAG in Verbindung mit semantischer SucheDie Ursprünge von RAGIm Jahr 2020 veröffentlichtePatrick Lewismit seinem Team von Meta AI Research das Paper"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". Darin beschrieben sie das RAG-Modell, das vortrainierte Sprachmodelle mit einer externen Wissensbasis kombiniert. Diese Wissensbasis nutzteDense Passage Retrieval(DPR), wobei Wikipedia-Artikel als Vektorindex dienten.Patrick Lewis - Der RAG DaddyDas zentrale Ziel von RAG war jedoch nicht die Vektorsuche selbst, sondern die Nutzungexterner Wissensquellen, um die Genauigkeit und Aktualität generierter Texte zu verbessern. Die konkrete Implementierung durch DPR war nur eine von vielen möglichen Varianten.Herausforderungen der Semantischen SucheWarum wird semantische Suche oft in Verbindung mit RAG gebracht? Weil sie es ermöglicht, natürliche Sprache zu verstehen und nicht nur nach Keywords zu suchen. So wie wir es von Sprachmodellen lieben gelernt haben. Doch sie bringterhebliche Herausforderungenmit sich:Nur Ähnlichkeiten, keine exakten Treffer: Die Suche basiert auf Ähnlichkeiten - exakte Begriffe, nach denen gesucht wird, können in den Ergebnissen fehlen.Qualität der Embedding-Modelle: Die Leistungsfähigkeit der Modelle, die Texte in Vektoren umwandeln, bestimmt die Suchqualität - eine Optimierung ist aufwendig.Vektordatenbanken beeinflussen das Ergebnis stark: Jede Datenbank hat ihre eigenen Stärken und Schwächen, was die Relevanz der Ergebnisse ebenfalls beeinflusst.Lock-in-Effekt bei Embedding-Modellen: Ein Wechsel des Modells erfordert eine vollständige Neuerstellung der Vektorisierung aller Daten.Die Semantische Suche ist nicht per se schlecht - sie kann sinnvoll sein, für spezielle Anforderungen. Die größte Herausforderung besteht darin, dass ihre Funktionsweise an verschiedenen Stellen beeinflusst wird: Ist das Embedding-Modell unzureichend? Sind die Daten schlecht geschnitten (gechunkt)? Liegt es an der Vektordatenbank?Das Herausfinden der eigentlichen Fehlerquelle ist aufwändig und sehr schwer messbar.Für bestimmte Einsatzzwecke kann die semantische Suche hervorragend sein - insbesondere in Kombination mit einem Hybrid-Ansatz (Keyword- + semantische Suche).In vielen Fällen jedoch reicht eine traditionelle, klassische Suche völlig aus und vermeidet unnötige Komplexität.Was RAG wirklich bedeutetWie bereits erwähnt, geht es bei RAG lediglich darum,externe Datenquellen in die KI-Generierung einzubinden. Dies kann mit oder ohne semantische Suche erfolgen.Schon lange bevor RAG populär wurde, haben wir in unserer Twitch-Community„My Coding Zone“eine YouTube-Integration entwickelt. Dabei erzeugte der Prompt automatisch Keywords für eine YouTube-Suche und lieferte die Ergebnisse an das Modell zurück. Das Sprachmodell antwortete daraufhin, als hätte es direkten Zugriff auf alle unsere YouTube-Folgen.RAG mit YouTube-API + Keyword-SucheAuch in Unternehmen sind relevante Daten oft bereits verfügbar - nur nicht in „sexy“ Form. Doch das ist kein Problem: Eine klassische Datenbanksuche kann in vielen Fällen völlig ausreichen, um dem Modell relevante Informationen bereitzustellen.Möglichkeiten, RAG ohne Vektordatenbanken zu nutzen:Webseiten (Extranet/Intranet)Klassische DatenbanksuchenAPI-AbfragenDokumentenmanagement-SystemeCRM- oder ERP-SystemeLokale DateienFazitEs gibt unzählige „Hello World“-Tutorials zu RAG, die oft die semantische Suche als Standardlösung präsentieren. In kleinen Beispielen funktioniert das wunderbar, doch in der Realität bringt sie erhebliche Herausforderungen mit sich. Viele dieser Tutorials gehen nicht darauf ein, dass alternative Methoden oft praktikabler sind. Gerade in echten Projekten zeigt sich, dass klassische Suchansätze oder hybride Lösungen (Keyword- + semantische Suche) häufig effektiver sind als die reine semantische Suche.Meine Erfahrung aus Kundenprojekten zeigt, dass oft traditionelle Suchmethoden völlig ausreichen und viel Komplexität ersparen. Wo eine semantische Suche Sinn macht, haben wir sie gezielt in Hybrid-Ansätzen kombiniert - mit großem Erfolg.Wie sieht es bei euch aus? Nutzt ihr RAG mit oder ohne semantische Suche?Wenn ihr mit der semantischen Suche gearbeitet habt, seid ihr dabei ebenfalls auf eine meiner erwähnten Herausforderungen gestoßen?Ich bin gespannt auf eure Erfahrungen! 🚀

RAG: Das Entwurfsmuster für KI-gestützte Unternehmensdaten

## RAG: Das Entwurfsmuster für KI-gestützte Unternehmensdaten

RAG: Das Entwurfsmuster für KI-gestützte Unternehmensdaten

Retrieval-Augmented Generation (RAG) ist ein leistungsstarkes Entwurfsmuster für die KI-Entwicklung. Es erweitert Sprachmodelle mit unternehmensspezifischen Daten, ohne dass ein eigenes KI-Modell trainiert werden muss.

Retrieval-Augmented Generation (RAG) ist ein leistungsstarkes Entwurfsmuster für die KI-Entwicklung. Es erweitert Sprachmodelle mit unternehmensspezifischen Daten, ohne dass ein eigenes KI-Modell trainiert werden muss.

Retrieval-Augmented Generation (RAG) ist ein leistungsstarkes Entwurfsmuster für die KI-Entwicklung. Es erweitert Sprachmodelle mit unternehmensspezifischen Daten, ohne dass ein eigenes KI-Modell trainiert werden muss.

Dabei kommt "indirekt" eine Technik namens „Few-Shot Learning“ aus dem Bereich des Prompt Engineerings zum Einsatz. Durch das Einbringen relevanter Informationen in den Prompt kann das Sprachmodell direkt auf diese zugreifen, wodurch die Wahrscheinlichkeit steigt, dass diese Daten zur Beantwortung genutzt werden. Dies reduziert Halluzinationen des Modells erheblich und die KI "kennt" eure Daten.

Dabei kommt "indirekt" eine Technik namens „Few-Shot Learning“ aus dem Bereich des Prompt Engineerings zum Einsatz. Durch das Einbringen relevanter Informationen in den Prompt kann das Sprachmodell direkt auf diese zugreifen, wodurch die Wahrscheinlichkeit steigt, dass diese Daten zur Beantwortung genutzt werden. Dies reduziert Halluzinationen des Modells erheblich und die KI "kennt" eure Daten.

Dabei kommt "indirekt" eine Technik namens „Few-Shot Learning“ aus dem Bereich des Prompt Engineerings zum Einsatz. Durch das Einbringen relevanter Informationen in den Prompt kann das Sprachmodell direkt auf diese zugreifen, wodurch die Wahrscheinlichkeit steigt, dass diese Daten zur Beantwortung genutzt werden. Dies reduziert Halluzinationen des Modells erheblich und die KI "kennt" eure Daten.

Few-Shot Learning - Notwendige Informationen sind im Prompt enthalten

Few-Shot Learning - Notwendige Informationen sind im Prompt enthalten

Das Besondere an RAG ist, dass der Benutzerprompt im Hintergrund automatisch vom System erweitert wird -ohne dass der Nutzer dies bemerkt. Viele Artikel und Tutorials erklären dies anhand der Vektorisierung von Eingaben und deren Vergleich mit einer Vektordatenbank - ein Prozess, der als„Semantische Suche“bekannt ist. Falls du mehr über Vektordaten und semantische Suche erfahren möchtest, schau dir meine bisherigenLinkedIn-Postsan.

Das Besondere an RAG ist, dass der Benutzerprompt im Hintergrund automatisch vom System erweitert wird -ohne dass der Nutzer dies bemerkt. Viele Artikel und Tutorials erklären dies anhand der Vektorisierung von Eingaben und deren Vergleich mit einer Vektordatenbank - ein Prozess, der als„Semantische Suche“bekannt ist. Falls du mehr über Vektordaten und semantische Suche erfahren möchtest, schau dir meine bisherigenLinkedIn-Postsan.

Das Besondere an RAG ist, dass der Benutzerprompt im Hintergrund automatisch vom System erweitert wird -

ohne dass der Nutzer dies bemerkt

. Viele Artikel und Tutorials erklären dies anhand der Vektorisierung von Eingaben und deren Vergleich mit einer Vektordatenbank - ein Prozess, der als

bekannt ist. Falls du mehr über Vektordaten und semantische Suche erfahren möchtest, schau dir meine bisherigen

Typische Illustration von RAG in Verbindung mit semantischer Suche

Typische Illustration von RAG in Verbindung mit semantischer Suche

Die Ursprünge von RAG

## Die Ursprünge von RAG

Die Ursprünge von RAG

Im Jahr 2020 veröffentlichtePatrick Lewismit seinem Team von Meta AI Research das Paper"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". Darin beschrieben sie das RAG-Modell, das vortrainierte Sprachmodelle mit einer externen Wissensbasis kombiniert. Diese Wissensbasis nutzteDense Passage Retrieval(DPR), wobei Wikipedia-Artikel als Vektorindex dienten.

Im Jahr 2020 veröffentlichtePatrick Lewismit seinem Team von Meta AI Research das Paper"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". Darin beschrieben sie das RAG-Modell, das vortrainierte Sprachmodelle mit einer externen Wissensbasis kombiniert. Diese Wissensbasis nutzteDense Passage Retrieval(DPR), wobei Wikipedia-Artikel als Vektorindex dienten.

Im Jahr 2020 veröffentlichte

mit seinem Team von Meta AI Research das Paper

"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"

. Darin beschrieben sie das RAG-Modell, das vortrainierte Sprachmodelle mit einer externen Wissensbasis kombiniert. Diese Wissensbasis nutzte

Dense Passage Retrieval

(DPR), wobei Wikipedia-Artikel als Vektorindex dienten.

Patrick Lewis - Der RAG Daddy

Patrick Lewis - Der RAG Daddy

Das zentrale Ziel von RAG war jedoch nicht die Vektorsuche selbst, sondern die Nutzungexterner Wissensquellen, um die Genauigkeit und Aktualität generierter Texte zu verbessern. Die konkrete Implementierung durch DPR war nur eine von vielen möglichen Varianten.

Das zentrale Ziel von RAG war jedoch nicht die Vektorsuche selbst, sondern die Nutzungexterner Wissensquellen, um die Genauigkeit und Aktualität generierter Texte zu verbessern. Die konkrete Implementierung durch DPR war nur eine von vielen möglichen Varianten.

Das zentrale Ziel von RAG war jedoch nicht die Vektorsuche selbst

, sondern die Nutzung

externer Wissensquellen

, um die Genauigkeit und Aktualität generierter Texte zu verbessern. Die konkrete Implementierung durch DPR war nur eine von vielen möglichen Varianten.

Herausforderungen der Semantischen Suche

## Herausforderungen der Semantischen Suche

Herausforderungen der Semantischen Suche

Warum wird semantische Suche oft in Verbindung mit RAG gebracht? Weil sie es ermöglicht, natürliche Sprache zu verstehen und nicht nur nach Keywords zu suchen. So wie wir es von Sprachmodellen lieben gelernt haben. Doch sie bringterhebliche Herausforderungenmit sich:

Warum wird semantische Suche oft in Verbindung mit RAG gebracht? Weil sie es ermöglicht, natürliche Sprache zu verstehen und nicht nur nach Keywords zu suchen. So wie wir es von Sprachmodellen lieben gelernt haben. Doch sie bringterhebliche Herausforderungenmit sich:

Warum wird semantische Suche oft in Verbindung mit RAG gebracht? Weil sie es ermöglicht, natürliche Sprache zu verstehen und nicht nur nach Keywords zu suchen. So wie wir es von Sprachmodellen lieben gelernt haben. Doch sie bringt

erhebliche Herausforderungen

Nur Ähnlichkeiten, keine exakten Treffer: Die Suche basiert auf Ähnlichkeiten - exakte Begriffe, nach denen gesucht wird, können in den Ergebnissen fehlen.Qualität der Embedding-Modelle: Die Leistungsfähigkeit der Modelle, die Texte in Vektoren umwandeln, bestimmt die Suchqualität - eine Optimierung ist aufwendig.Vektordatenbanken beeinflussen das Ergebnis stark: Jede Datenbank hat ihre eigenen Stärken und Schwächen, was die Relevanz der Ergebnisse ebenfalls beeinflusst.Lock-in-Effekt bei Embedding-Modellen: Ein Wechsel des Modells erfordert eine vollständige Neuerstellung der Vektorisierung aller Daten.

Nur Ähnlichkeiten, keine exakten Treffer: Die Suche basiert auf Ähnlichkeiten - exakte Begriffe, nach denen gesucht wird, können in den Ergebnissen fehlen.

Nur Ähnlichkeiten, keine exakten Treffer

: Die Suche basiert auf Ähnlichkeiten - exakte Begriffe, nach denen gesucht wird, können in den Ergebnissen fehlen.

Qualität der Embedding-Modelle: Die Leistungsfähigkeit der Modelle, die Texte in Vektoren umwandeln, bestimmt die Suchqualität - eine Optimierung ist aufwendig.

Qualität der Embedding-Modelle

: Die Leistungsfähigkeit der Modelle, die Texte in Vektoren umwandeln, bestimmt die Suchqualität - eine Optimierung ist aufwendig.

Vektordatenbanken beeinflussen das Ergebnis stark: Jede Datenbank hat ihre eigenen Stärken und Schwächen, was die Relevanz der Ergebnisse ebenfalls beeinflusst.

Vektordatenbanken beeinflussen das Ergebnis stark

: Jede Datenbank hat ihre eigenen Stärken und Schwächen, was die Relevanz der Ergebnisse ebenfalls beeinflusst.

Lock-in-Effekt bei Embedding-Modellen: Ein Wechsel des Modells erfordert eine vollständige Neuerstellung der Vektorisierung aller Daten.

Lock-in-Effekt bei Embedding-Modellen

: Ein Wechsel des Modells erfordert eine vollständige Neuerstellung der Vektorisierung aller Daten.

Die Semantische Suche ist nicht per se schlecht - sie kann sinnvoll sein, für spezielle Anforderungen. Die größte Herausforderung besteht darin, dass ihre Funktionsweise an verschiedenen Stellen beeinflusst wird: Ist das Embedding-Modell unzureichend? Sind die Daten schlecht geschnitten (gechunkt)? Liegt es an der Vektordatenbank?Das Herausfinden der eigentlichen Fehlerquelle ist aufwändig und sehr schwer messbar.

Die Semantische Suche ist nicht per se schlecht - sie kann sinnvoll sein, für spezielle Anforderungen. Die größte Herausforderung besteht darin, dass ihre Funktionsweise an verschiedenen Stellen beeinflusst wird: Ist das Embedding-Modell unzureichend? Sind die Daten schlecht geschnitten (gechunkt)? Liegt es an der Vektordatenbank?Das Herausfinden der eigentlichen Fehlerquelle ist aufwändig und sehr schwer messbar.

Die Semantische Suche ist nicht per se schlecht - sie kann sinnvoll sein, für spezielle Anforderungen. Die größte Herausforderung besteht darin, dass ihre Funktionsweise an verschiedenen Stellen beeinflusst wird: Ist das Embedding-Modell unzureichend? Sind die Daten schlecht geschnitten (gechunkt)? Liegt es an der Vektordatenbank?

Das Herausfinden der eigentlichen Fehlerquelle ist aufwändig und sehr schwer messbar.

Für bestimmte Einsatzzwecke kann die semantische Suche hervorragend sein - insbesondere in Kombination mit einem Hybrid-Ansatz (Keyword- + semantische Suche).In vielen Fällen jedoch reicht eine traditionelle, klassische Suche völlig aus und vermeidet unnötige Komplexität.

Für bestimmte Einsatzzwecke kann die semantische Suche hervorragend sein - insbesondere in Kombination mit einem Hybrid-Ansatz (Keyword- + semantische Suche).In vielen Fällen jedoch reicht eine traditionelle, klassische Suche völlig aus und vermeidet unnötige Komplexität.

Für bestimmte Einsatzzwecke kann die semantische Suche hervorragend sein - insbesondere in Kombination mit einem Hybrid-Ansatz (Keyword- + semantische Suche).

In vielen Fällen jedoch reicht eine traditionelle, klassische Suche völlig aus und vermeidet unnötige Komplexität.

Was RAG wirklich bedeutet

## Was RAG wirklich bedeutet

Was RAG wirklich bedeutet

Wie bereits erwähnt, geht es bei RAG lediglich darum,externe Datenquellen in die KI-Generierung einzubinden. Dies kann mit oder ohne semantische Suche erfolgen.

Wie bereits erwähnt, geht es bei RAG lediglich darum,externe Datenquellen in die KI-Generierung einzubinden. Dies kann mit oder ohne semantische Suche erfolgen.

Wie bereits erwähnt, geht es bei RAG lediglich darum,

externe Datenquellen in die KI-Generierung einzubinden

. Dies kann mit oder ohne semantische Suche erfolgen.

Schon lange bevor RAG populär wurde, haben wir in unserer Twitch-Community„My Coding Zone“eine YouTube-Integration entwickelt. Dabei erzeugte der Prompt automatisch Keywords für eine YouTube-Suche und lieferte die Ergebnisse an das Modell zurück. Das Sprachmodell antwortete daraufhin, als hätte es direkten Zugriff auf alle unsere YouTube-Folgen.

Schon lange bevor RAG populär wurde, haben wir in unserer Twitch-Community„My Coding Zone“eine YouTube-Integration entwickelt. Dabei erzeugte der Prompt automatisch Keywords für eine YouTube-Suche und lieferte die Ergebnisse an das Modell zurück. Das Sprachmodell antwortete daraufhin, als hätte es direkten Zugriff auf alle unsere YouTube-Folgen.

Schon lange bevor RAG populär wurde, haben wir in unserer Twitch-Community

eine YouTube-Integration entwickelt. Dabei erzeugte der Prompt automatisch Keywords für eine YouTube-Suche und lieferte die Ergebnisse an das Modell zurück. Das Sprachmodell antwortete daraufhin, als hätte es direkten Zugriff auf alle unsere YouTube-Folgen.

RAG mit YouTube-API + Keyword-Suche

RAG mit YouTube-API + Keyword-Suche

Auch in Unternehmen sind relevante Daten oft bereits verfügbar - nur nicht in „sexy“ Form. Doch das ist kein Problem: Eine klassische Datenbanksuche kann in vielen Fällen völlig ausreichen, um dem Modell relevante Informationen bereitzustellen.

Auch in Unternehmen sind relevante Daten oft bereits verfügbar - nur nicht in „sexy“ Form. Doch das ist kein Problem: Eine klassische Datenbanksuche kann in vielen Fällen völlig ausreichen, um dem Modell relevante Informationen bereitzustellen.

Auch in Unternehmen sind relevante Daten oft bereits verfügbar - nur nicht in „sexy“ Form. Doch das ist kein Problem: Eine klassische Datenbanksuche kann in vielen Fällen völlig ausreichen, um dem Modell relevante Informationen bereitzustellen.

Möglichkeiten, RAG ohne Vektordatenbanken zu nutzen:

### Möglichkeiten, RAG ohne Vektordatenbanken zu nutzen:

Möglichkeiten, RAG ohne Vektordatenbanken zu nutzen:

Webseiten (Extranet/Intranet)Klassische DatenbanksuchenAPI-AbfragenDokumentenmanagement-SystemeCRM- oder ERP-SystemeLokale Dateien

Webseiten (Extranet/Intranet)

Webseiten (Extranet/Intranet)

Klassische Datenbanksuchen

Klassische Datenbanksuchen

Dokumentenmanagement-Systeme

Dokumentenmanagement-Systeme

CRM- oder ERP-Systeme

CRM- oder ERP-Systeme

Es gibt unzählige „Hello World“-Tutorials zu RAG, die oft die semantische Suche als Standardlösung präsentieren. In kleinen Beispielen funktioniert das wunderbar, doch in der Realität bringt sie erhebliche Herausforderungen mit sich. Viele dieser Tutorials gehen nicht darauf ein, dass alternative Methoden oft praktikabler sind. Gerade in echten Projekten zeigt sich, dass klassische Suchansätze oder hybride Lösungen (Keyword- + semantische Suche) häufig effektiver sind als die reine semantische Suche.

Es gibt unzählige „Hello World“-Tutorials zu RAG, die oft die semantische Suche als Standardlösung präsentieren. In kleinen Beispielen funktioniert das wunderbar, doch in der Realität bringt sie erhebliche Herausforderungen mit sich. Viele dieser Tutorials gehen nicht darauf ein, dass alternative Methoden oft praktikabler sind. Gerade in echten Projekten zeigt sich, dass klassische Suchansätze oder hybride Lösungen (Keyword- + semantische Suche) häufig effektiver sind als die reine semantische Suche.

Es gibt unzählige „Hello World“-Tutorials zu RAG, die oft die semantische Suche als Standardlösung präsentieren. In kleinen Beispielen funktioniert das wunderbar, doch in der Realität bringt sie erhebliche Herausforderungen mit sich. Viele dieser Tutorials gehen nicht darauf ein, dass alternative Methoden oft praktikabler sind. Gerade in echten Projekten zeigt sich, dass klassische Suchansätze oder hybride Lösungen (Keyword- + semantische Suche) häufig effektiver sind als die reine semantische Suche.

Meine Erfahrung aus Kundenprojekten zeigt, dass oft traditionelle Suchmethoden völlig ausreichen und viel Komplexität ersparen. Wo eine semantische Suche Sinn macht, haben wir sie gezielt in Hybrid-Ansätzen kombiniert - mit großem Erfolg.

Meine Erfahrung aus Kundenprojekten zeigt, dass oft traditionelle Suchmethoden völlig ausreichen und viel Komplexität ersparen. Wo eine semantische Suche Sinn macht, haben wir sie gezielt in Hybrid-Ansätzen kombiniert - mit großem Erfolg.

Meine Erfahrung aus Kundenprojekten zeigt, dass oft traditionelle Suchmethoden völlig ausreichen und viel Komplexität ersparen. Wo eine semantische Suche Sinn macht, haben wir sie gezielt in Hybrid-Ansätzen kombiniert - mit großem Erfolg.

Wie sieht es bei euch aus? Nutzt ihr RAG mit oder ohne semantische Suche?

### Wie sieht es bei euch aus? Nutzt ihr RAG mit oder ohne semantische Suche?

Wie sieht es bei euch aus? Nutzt ihr RAG mit oder ohne semantische Suche?

Wenn ihr mit der semantischen Suche gearbeitet habt, seid ihr dabei ebenfalls auf eine meiner erwähnten Herausforderungen gestoßen?

### Wenn ihr mit der semantischen Suche gearbeitet habt, seid ihr dabei ebenfalls auf eine meiner erwähnten Herausforderungen gestoßen?

Wenn ihr mit der semantischen Suche gearbeitet habt, seid ihr dabei ebenfalls auf eine meiner erwähnten Herausforderungen gestoßen?

Ich bin gespannt auf eure Erfahrungen! 🚀

### Ich bin gespannt auf eure Erfahrungen! 🚀

Ich bin gespannt auf eure Erfahrungen! 🚀

LikeComment1715 Comments

LikeComment1715 Comments

Gregor Biswanger✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer4moReport this commentJETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8ULikeReply1 ReactionRalf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentIch glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.LikeReply2 Reactions3 ReactionsRalf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentDu willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.LikeReply2 Reactions3 ReactionsLeonhard FischlLead Software Architect bei EXXETA AG8moReport this commentPhilipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?LikeReply1 Reaction2 ReactionsChristian HeyerKI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz8moReport this commentDas Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.LikeReply1 Reaction2 ReactionsSee more comments

Gregor Biswanger✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer4moReport this commentJETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8ULikeReply1 ReactionRalf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentIch glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.LikeReply2 Reactions3 ReactionsRalf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentDu willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.LikeReply2 Reactions3 ReactionsLeonhard FischlLead Software Architect bei EXXETA AG8moReport this commentPhilipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?LikeReply1 Reaction2 ReactionsChristian HeyerKI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz8moReport this commentDas Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.LikeReply1 Reaction2 ReactionsSee more comments

Gregor Biswanger✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer4moReport this commentJETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8ULikeReply1 Reaction

Gregor Biswanger✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer4moReport this commentJETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8U

Gregor Biswanger✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer4moReport this comment

✨ Generative AI-Berater & Trainer | Microsoft MVP für Azure AI | Maßgeschneiderte KI-Lösungen für digitale Transformation | Keynote Speaker | YouTuber & Twitch Live-Streamer

JETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8U

JETZT gibt es auch das passende VIDEO zu diesem Artikel auf YOUTUBE... Viel Spaß beim Ansehen...https://youtu.be/D9XSwJClj8U

Ralf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentIch glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.LikeReply2 Reactions3 Reactions

Ralf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentIch glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.

Ralf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this comment

Unabhängig beschäftigt als Berater, Coach, Trainer

Ich glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.

Ich glaube, es hilft, noch genauer hinzuschauen: gehts um strukturierte und unstrukturierte Daten?

Bei unstrukturierten (zb Bücher, Artikel usw.) kommt kaum etwas anderes als semantic search in Frage, würde ich sagen. (Auch da hat sie natürlich ihre Grenzen je nach Fragestellung und Umfang der Daten in Relation zum Kontextfenster.)

Bei strukturierten Daten hingegen ist semantic search eher nur ein weiterer Query-Operator. Es gab schon fuzzy search Operatoren, nun kommen noch embeddings dazu.

Umgekehrt: Manchmal kann man gar keins semantic search einsetzen, weil es einen spezifischen API einfach gibt. Denn jedoch überhaupt einzubinden, ist eben auch RAG.

Ergo: RAG ist einfach nur der Begriff für eine Menge von Maßnahmen, mit denen man einen Kontext um Daten anreichern kann.

LikeReply2 Reactions3 Reactions

Ralf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentDu willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.LikeReply2 Reactions3 Reactions

Ralf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this commentDu willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.

Ralf WestphalUnabhängig beschäftigt als Berater, Coach, Trainer8moReport this comment

Unabhängig beschäftigt als Berater, Coach, Trainer

Du willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.

Du willst also sagen: "Retrieval" kann alles mögliche sein? Ich kann also zb einen GPT schreiben, der per REST auf eine Datenbank zugreift und JSON Dokumente holt, die werden dann in den Kontext eingebunden und die KI macht gem. Prompt damit etwas.

Das JSON wurde "retrievet" und "augmentet" die "generation".

Es muss nicht immer das Prompt in ein Embedding umgewandelt werden, um damit ähnliche Chunks aus einer Vektordatenbank zu holen.

Das R in RAG sollte man weiter fassen? Da bin ich dabei. Mit TypingMind und Plugins ist das z.B. sehr einfach möglich.

LikeReply2 Reactions3 Reactions

Leonhard FischlLead Software Architect bei EXXETA AG8moReport this commentPhilipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?LikeReply1 Reaction2 Reactions

Leonhard FischlLead Software Architect bei EXXETA AG8moReport this commentPhilipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?

Leonhard FischlLead Software Architect bei EXXETA AG8moReport this comment

Lead Software Architect bei EXXETA AG

Philipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?

Philipp Michalik,André LindenbergSehr spannend wie sich das Thema grad entwickelt.
Wie seht ihr beiden den Ansatz vonGregor Biswanger?

LikeReply1 Reaction2 Reactions

Christian HeyerKI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz8moReport this commentDas Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.LikeReply1 Reaction2 Reactions

Christian HeyerKI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz8moReport this commentDas Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.

Christian HeyerKI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz8moReport this comment

KI-Lösungen: Automatisierung, Beratung & Schulungen | CEO RedOrbit GmbH | Effizienz durch Künstliche Intelligenz

Das Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.

Das Problem an der semantischen Suche im RAG Kontext ist ja, dass nicht zwingend der Kontext der Frage des Users erkannt wird (werden kann) und deshalb ggf. irrelevante Chunks aus der Vektordatenbank gezogen und an das Llm übergeben werden. 

Wie ihr das Problem mit einer klassischen Keywortsuche löst würde mich sehr interessieren.

LikeReply1 Reaction2 Reactions

To view or add a comment,sign in

## More articles by Gregor Biswanger

The Danger of MCP - What Every Developer Needs to Know 🚨Apr 17, 2025The Danger of MCP - What Every Developer Needs to Know 🚨It sounds like a smart solution. It promises efficiency and new possibilities.4610 Comments

The Danger of MCP - What Every Developer Needs to Know 🚨Apr 17, 2025The Danger of MCP - What Every Developer Needs to Know 🚨It sounds like a smart solution. It promises efficiency and new possibilities.4610 Comments

The Danger of MCP - What Every Developer Needs to Know 🚨Apr 17, 2025The Danger of MCP - What Every Developer Needs to Know 🚨It sounds like a smart solution. It promises efficiency and new possibilities.4610 Comments

The Danger of MCP - What Every Developer Needs to Know 🚨

Apr 17, 2025The Danger of MCP - What Every Developer Needs to Know 🚨It sounds like a smart solution. It promises efficiency and new possibilities.4610 Comments

### The Danger of MCP - What Every Developer Needs to Know 🚨

It sounds like a smart solution. It promises efficiency and new possibilities.

## Explore content categories

CareerProductivityFinanceSoft Skills & Emotional IntelligenceProject ManagementEducationTechnologyLeadershipEcommerceUser ExperienceRecruitment & HRCustomer ExperienceReal EstateMarketingSalesRetail & MerchandisingScienceSupply Chain ManagementFuture Of WorkConsultingWritingEconomicsArtificial IntelligenceEmployee ExperienceWorkplace TrendsFundraisingNetworkingCorporate Social ResponsibilityNegotiationCommunicationEngineeringHospitality & TourismBusiness StrategyChange ManagementOrganizational CultureDesignInnovationEvent PlanningTraining & DevelopmentShow moreShow less

CareerProductivityFinanceSoft Skills & Emotional IntelligenceProject ManagementEducationTechnologyLeadershipEcommerceUser ExperienceRecruitment & HRCustomer ExperienceReal EstateMarketingSalesRetail & MerchandisingScienceSupply Chain ManagementFuture Of WorkConsultingWritingEconomicsArtificial IntelligenceEmployee ExperienceWorkplace TrendsFundraisingNetworkingCorporate Social ResponsibilityNegotiationCommunicationEngineeringHospitality & TourismBusiness StrategyChange ManagementOrganizational CultureDesignInnovationEvent PlanningTraining & DevelopmentShow moreShow less

Soft Skills & Emotional Intelligence

Retail & Merchandising

Supply Chain Management

Artificial Intelligence

Corporate Social Responsibility

Hospitality & Tourism

Organizational Culture

Training & Development

