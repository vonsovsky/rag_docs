import os

from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from langchain.schema.document import Document
from langchain.text_splitter import CharacterTextSplitter

from src.llm import Prompt
from src.models import KnowledgeBase

basepath = os.path.dirname(os.path.realpath(__file__))
datapath = os.path.join(basepath, "../data")

router = APIRouter()
kb = KnowledgeBase(datapath)
prompt = Prompt(kb)


@router.get("/")
def read_root():
    return "A Simple RAG app"


# TODO move this to unified helper function
def get_text_chunks_langchain(text):
    text_splitter = CharacterTextSplitter(chunk_size=kb.CHUNK_SIZE, chunk_overlap=kb.CHUNK_OVERLAP)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    return docs


@router.post("/upload/")
async def answer_by_doc(file: UploadFile = File(...)):
    content = await file.read()
    docs = get_text_chunks_langchain(content.decode('utf-8'))
    answers = [prompt.answer(doc.page_content) for doc in docs]

    return JSONResponse(content={
        "answers": answers,
    })
