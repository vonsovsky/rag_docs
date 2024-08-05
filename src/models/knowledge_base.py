from src.logger import Logger

from chromadb.config import Settings
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

logger = Logger()


class KnowledgeBase:

    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    def __init__(self, source_folder_path: str) -> None:
        self.docs = None
        self.load(source_folder_path=source_folder_path)
        self.vectorstore = self.docs_to_embeddings(
            chunked_docs=self.split_documents(),
            embedder=OpenAIEmbeddings()
        )
        logger.info("Knowledge base loaded.")

    def load(self, source_folder_path: str):
        loader = DirectoryLoader(
            path=source_folder_path
        )
        self.docs = loader.load()

    def split_documents(
            self,
    ):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.CHUNK_SIZE,
            chunk_overlap=self.CHUNK_OVERLAP,
        )
        chunked_docs = splitter.split_documents(self.docs)
        return chunked_docs

    def docs_to_embeddings(
            self, chunked_docs, embedder
    ):
        return Chroma.from_documents(documents=chunked_docs, embedding=embedder)
