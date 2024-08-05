from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

from src.llm import Prompt
from src.models import KnowledgeBase

router = APIRouter()
kb = KnowledgeBase()
prompt = Prompt(kb)


@router.get("/")
def read_root():
    return "A Simple RAG app"


@router.post("/upload/")
async def answer_by_doc(file: UploadFile = File(...)):
    content = await file.read()
    #prompt.answer(content)
    answer = prompt.answer("What is Task Decomposition?")

    return JSONResponse(content={
        "answer": answer,
    })
