import logging
import os
import sys

from langchain_core.documents import Document
from langchain_unstructured import UnstructuredLoader

from advanced_rag.backend.services.document_source import DocumentSource


class LibmagicWarningFilter(logging.Filter):
    def filter(self, record):
        return 'libmagic is unavailable' not in record.getMessage()


class FileProcessor:
    @staticmethod
    def load_documents(
            document_source: DocumentSource,
    ) -> list[Document]:
        logging.info("Loading documents from "+document_source+" dump")
        
        unstructured_logger = logging.getLogger('unstructured')
        libmagic_filter = LibmagicWarningFilter()
        unstructured_logger.addFilter(libmagic_filter)
        
        file_paths: list[str] = FileProcessor.get_all_files(document_source)
        loader = UnstructuredLoader(
            file_paths,
            chunking_strategy="basic",
            max_characters=sys.maxsize,
            include_orig_elements=False,
        )
        documents = loader.load()
        
        unstructured_logger.removeFilter(libmagic_filter)

        for document in documents:
            document.metadata["source"] = FileProcessor.normalize_path(document.metadata["source"], document_source)
        return documents

    @staticmethod
    def get_all_files(
            document_source: DocumentSource,
    ):
        all_files = []
        path = document_source.path
        for root, _, files in os.walk(path):
            for file in files:
                if FileProcessor._is_processed(file):
                    all_files.append(os.path.join(root, file))
        return all_files

    @staticmethod
    def _is_processed(
            file: str,
    ):
        lower_file = file.lower()
        return ('.DS_Store'.lower() not in lower_file and
                'README'.lower() not in lower_file)

    @staticmethod
    def normalize_path(
            path: str,
            document_source: DocumentSource,
    ):
        return (path
                .replace("\\", "/")
                .replace(document_source.path + "/", ""))
