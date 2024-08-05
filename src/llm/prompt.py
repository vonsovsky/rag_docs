import os

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

from src.models import KnowledgeBase


class Prompt:

    def __init__(self, kb: KnowledgeBase):
        self.retriever = kb.vectorstore.as_retriever()
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.prompt = hub.pull("rlm/rag-prompt")

    @staticmethod
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def answer(self, question) -> str:
        rag_chain = (
                {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
                | self.prompt
                | self.llm
                | StrOutputParser()
        )

        return rag_chain.invoke(question)
