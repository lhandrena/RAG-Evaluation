print("=" * 80)
print("RAGAS Testset Generator - Übung gestartet")
print("=" * 80)
print("Lade benötigte Module...")
print()

import asyncio
import sys
from typing import List

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_unstructured import UnstructuredLoader
from ragas.llms.base import LangchainLLMWrapper
from ragas.embeddings.base import embedding_factory
from ragas.run_config import RunConfig
from ragas.testset import TestsetGenerator
from ragas.testset.persona import Persona
from ragas.testset.synthesizers import SingleHopSpecificQuerySynthesizer


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    load_dotenv()

    print("=" * 80)
    print("RAGAS Testset Generator - Übung")
    print("=" * 80)
    print()

    article_path = "src/advanced_rag/scraping/tagesschau_dump/2025-03-14/wirtschaft/article_7.md"
    
    print(f"Schritt 1: Lade Artikel")
    print(f"  Pfad: {article_path}")
    
    loader = UnstructuredLoader(
        [article_path],
        chunking_strategy="basic",
    )
    documents: List[Document] = loader.load()
    print(f"  ✓ {len(documents)} Dokument-Chunks geladen")
    print()

    print("Schritt 2: Initialisiere LLM und Embeddings")
    run_config = RunConfig(max_workers=2, max_retries=6, max_wait=20, timeout=180)
    openai_chat = ChatOpenAI(
        model="gpt-4o-mini",
        timeout=run_config.timeout,
        max_retries=0,
    )
    generator_llm = LangchainLLMWrapper(
        openai_chat,
        run_config=run_config,
    )
    generator_embeddings = embedding_factory(
        provider="openai",
        model="text-embedding-3-large"
    )
    print("  ✓ LLM: gpt-4o-mini")
    print("  ✓ Embeddings: text-embedding-3-large")
    print()

    print("Schritt 3: Definiere Persona")
    personas = [
        Persona(
            name="Wirtschaftsstudent",
            role_description="Ein Student, der sich für Wirtschaft und Finanzmärkte interessiert",
        ),
    ]
    print(f"  ✓ Persona: {personas[0].name}")
    print(f"    Beschreibung: {personas[0].role_description}")
    print()

    print("Schritt 4: Erstelle TestsetGenerator")
    generator = TestsetGenerator(
        llm=generator_llm,
        embedding_model=generator_embeddings,
        persona_list=personas,
    )
    print("  ✓ Generator initialisiert")
    print()

    print("Schritt 5: Definiere Query-Synthesizer")
    distribution = [
        (SingleHopSpecificQuerySynthesizer(llm=generator_llm), 1.0)
    ]
    print("  ✓ SingleHopSpecificQuerySynthesizer (100%)")
    print()

    print("Schritt 6: Generiere Testdatensatz")
    print("  (Dies kann einige Minuten dauern...)")
    print()
    
    dataset = generator.generate_with_langchain_docs(
        documents,
        testset_size=1,
        query_distribution=distribution,
        run_config=run_config,
    )
    print("  ✓ Datensatz generiert")
    print()

    print("=" * 80)
    print("ERGEBNIS")
    print("=" * 80)
    print()
    
    eval_dataset = dataset.to_evaluation_dataset()
    if len(eval_dataset) == 0:
        print("Keine Samples generiert. Bitte RAGAS-Logs prüfen.")
        sys.exit(1)
    print("Frage:")
    print(f"  {eval_dataset[0].user_input}")
    print()
    print("Antwort:")
    print(f"  {eval_dataset[0].reference}")
    print()
    
    print("=" * 80)
