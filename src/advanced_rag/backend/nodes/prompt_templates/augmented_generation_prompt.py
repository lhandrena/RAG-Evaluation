from pathlib import Path


class AugmentedGenerationPrompt:

    @staticmethod
    def get_prompt() -> str:
        prompt_file = Path(__file__).parent / "generation_prompt_bad.txt"
        #prompt_file = Path(__file__).parent / "generation_prompt_good.txt"
        return prompt_file.read_text().strip()
