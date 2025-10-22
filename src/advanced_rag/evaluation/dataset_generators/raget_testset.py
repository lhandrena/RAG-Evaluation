import csv
import os
import warnings

import pandas as pd
from flask.cli import load_dotenv
from giskard.llm.client.litellm import LiteLLMClient
from giskard.llm.embeddings.litellm import LiteLLMEmbedding
from giskard.rag import KnowledgeBase, generate_testset
from giskard.rag.question_generators import complex_questions, simple_questions, distracting_questions, \
    situational_questions, double_questions, conversational_questions
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.file import UnstructuredReader

from services.document_source import DocumentSource
from services.file_processor import FileProcessor

document_source = DocumentSource.LLM_GENERAL_SURVEY_PAPER
chunk_size = 512
num_questions = 20
generators = [
    simple_questions,
    complex_questions,
    distracting_questions,
    situational_questions,
    double_questions,
    conversational_questions
]

datasets_base_path = "./datasets"

llm_model = "gpt-4.1"
embedding_model = 'text-embedding-3-large'
min_topic_size = 5

load_dotenv()
pd.set_option('display.max_colwidth', 400)
warnings.filterwarnings('ignore')


def load_or_create_knowledge_base_df(
        document_source: DocumentSource,
):
    knowledge_base_df_file = f'./knowledgebase/{document_source.lower()}/knowledge_base_df_{chunk_size}_chunk_size.csv'

    if os.path.isfile(knowledge_base_df_file):
        return pd.read_csv(knowledge_base_df_file)
    else:
        loader = UnstructuredReader()
        document_paths = FileProcessor.get_all_files(document_source)
        processed_documents = []

        print(f'Loading {len(document_paths)} documents.')
        for document_path in document_paths:
            documents = loader.load_data(file=document_path)
            assert (len(documents) == 1)
            document = documents[0]
            document.doc_id = FileProcessor.normalize_path(document_path, document_source)
            processed_documents.append(document)
            print(f'Loaded {len(processed_documents)} / {len(document_paths)} documents.')

        splitter = SentenceSplitter(chunk_size=chunk_size)
        text_nodes = splitter(processed_documents)
        df = pd.DataFrame(
            [(
                node.text,
                node.ref_doc_id
            ) for node in text_nodes],
            columns=[
                'text',
                'ref_doc_id',
            ],
        )
        df.to_csv(knowledge_base_df_file)
        return df


def extract_doc_ids_from(
        ts,
):
    samples_with_doc_ids = []
    unique_doc_ids = set()

    for sample in ts.samples:
        sample_with_doc_ids = extract_unique_doc_ids_from(sample)
        samples_with_doc_ids.append(sample_with_doc_ids)
        unique_doc_ids.update(sample_with_doc_ids[1])

    return samples_with_doc_ids, unique_doc_ids


def extract_unique_doc_ids_from(
        sample,
):
    unique_document_ids = set()
    document_splits = sample.reference_context.split('Document')

    for document_split in document_splits:
        if 'ref_doc_id:' in document_split:
            ref_doc_id_splits = document_split.split('ref_doc_id:')
            assert len(ref_doc_id_splits) == 2
            ref_doc_id = ref_doc_id_splits[1].strip()
            unique_document_ids.add(ref_doc_id)

    return (
        sample,
        unique_document_ids
    )


def create_csv_from(
        samples_with_doc_ids,
):
    return [create_dict_from(sample, doc_ids) for (
        sample,
        doc_ids
    ) in samples_with_doc_ids]


def create_dict_from(
        sample,
        doc_ids,
):
    return {
        'input':             sample.question,
        'expected_output':   sample.reference_answer,
        'expected_articles': append_string_from(doc_ids),
    }


def append_string_from(
        unique_document_ids,
):
    appended_document_ids = ''

    for unique_document_id in unique_document_ids:
        if appended_document_ids == '':
            appended_document_ids = f'{unique_document_id}'
        else:
            appended_document_ids = f'{appended_document_ids}|{unique_document_id}'

    return appended_document_ids


def save_testset_to_file(
        ts,
        csv_dict,
        num_topics,
        generator,
        document_source,
):
    base_path = f'{datasets_base_path}/{document_source.lower()}'
    jsonl_filename = f'{base_path}/jsonl/{create_file_name(document_source, num_topics, generator, 'jsonl')}'
    ts.save(jsonl_filename)

    csv_filename = f'{base_path}/csv/{create_file_name(document_source, num_topics, generator, 'csv')}'
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = [
            'input',
            'expected_output',
            'expected_articles',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_dict)


def create_file_name(
        document_source,
        num_topics,
        generator,
        file_extension,
):
    question_type = generator._question_type.replace(" ", "_")
    return f'{document_source.lower()}_{question_type}_generator_{num_questions}_questions_{num_topics}_topics.{file_extension}'


if __name__ == '__main__':
    knowledge_base_df = load_or_create_knowledge_base_df(document_source)

    knowledge_base = KnowledgeBase(
        data=knowledge_base_df,
        llm_client=LiteLLMClient(llm_model),
        embedding_model=LiteLLMEmbedding(embedding_model),
        min_topic_size=min_topic_size,
    )

    savable_data = knowledge_base.get_savable_data()
    num_topics = len(savable_data['topics'])

    for generator in generators:
        testset = generate_testset(
            knowledge_base,
            num_questions=num_questions,
            agent_description=f'''
            A chatbot generating simple, short and superficial questions about {document_source.topic}.
            ''',
            language='de',
            question_generators=[
                generator,
            ],
        )

        samples_with_doc_ids, unique_doc_ids = extract_doc_ids_from(testset)
        testset_dict = create_csv_from(samples_with_doc_ids)
        save_testset_to_file(testset, testset_dict, num_topics, generator, document_source)

        num_unique_doc_ids = len(unique_doc_ids)
        article_ids = set(knowledge_base_df.ref_doc_id)
        num_article_ids = len(article_ids)
        ratio = num_unique_doc_ids / num_article_ids

        print(f"Unique doc IDs: {num_unique_doc_ids}")
        print(f"Total doc IDs: {num_article_ids}")
        print(f'Ratio: {ratio:.2f}')
