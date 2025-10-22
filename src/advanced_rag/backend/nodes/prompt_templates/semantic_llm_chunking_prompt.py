import textwrap


class SemanticLlmChunkingPrompt:

    @staticmethod
    def get_prompt() -> str:
        prompt: str = textwrap.dedent(
            """
            ***Ziel***
            
            Du bist ein Experte, der sich darauf spezialisiert hat, Texte in thematisch konsistente Abschnitte zu unterteilen.
            Der Text wurde in Segmente unterteilt, die jeweils mit den Tags <chunk_X_start> und <chunk_X_end> markiert sind, wobei X die Segmentnummer ist.
            Deine Aufgabe ist es, die Punkte zu identifizieren, an denen Trennungen vorgenommen werden sollten, sodass aufeinanderfolgende Segmente mit ähnlichen Themen zusammenbleiben.

            ***Regeln:***
            
            - Segmente, die zusammen einen Satz beinhalten, gehören zusammen und dürfen nicht getrennt werden.
            - Alle Segmente, die auf ein Segment mit einer Markdown-Überschrift folgen und keinen eigenständigen inhaltlichen Bezug zu einem neuen Thema haben (z.B. leere oder nur Whitespaces enthaltende Segmente), gehören zur Überschrift.
            - Unterüberschriften gehören zum selben Segment der Hauptüberschrift, falls zwischen den Überschriften kein Text vorhanden ist. Dementsprechend dürfen die Segmente nicht voneinander getrennt werden.
            - Trenne nie nach einem Segment, wenn das darauf folgende Segment nur Whitespaces enthält.
            - Segmente, folgend auf ein Segment mit einer Überschrift, gehören zum Segment der Überschrift unabhängig davon, ob dazwischen Segmente sind, welche nur Whitespaces enthalten.
            - Segmente ohne Text und solche welche nur Whitespaces enthalten gehören immer zum vorherigen Segment.
            - Fokussiere dich bei der Trennung der Segmente auf ihren Inhalt und nicht auf Formatierungen wie z.B. Leerzeilen.
            - Folgen auf Segmente, die eine Frage ergeben, Segmente mit der zugehörigen Antwort, ergeben diese eine thematische Gruppe und es darf zwischen Frage und Antwort nicht getrennt werden.
            - Zwischen zwei thematisch verschiedenen Gruppen von Segmenten muss eine Trennung erfolgen.

            **Beispiel:**
            - Antworte mit einer Liste der Segment-IDs, an denen eine Trennung erfolgen sollte. Wenn beispielsweise die Segmente 1 und 2 zusammengehören, aber Segment 3 ein neues Thema beginnt, solltest du eine Trennung nach Segment 2 vorschlagen.

            <chunked_input>
                {chunked_input}
            </chunked_input>

            Your response should be in the following JSON, and **no other text**:
            <format_instructions>
                {format_instructions}
            </format_instructions>
            """,
        )
        return prompt.strip()

    @staticmethod
    def get_input_variables() -> list[str]:
        return [
            "chunked_input"
        ]

    @staticmethod
    def get_partial_variables(
            format_instructions: str,
    ) -> dict[str, str]:
        return {
            "format_instructions": format_instructions
        }
