# RAG docs

This FastAPI server accepts document on its endpoints and performs RAG using LangChain framework.

## Installation

The app was tested on Python 3.10. There were issues with SQLite package observed on version 3.8.

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Set up OPENAI_API_KEY environment variable

    export set up OPENAI_API_KEY=sk-****

Run FastAPI server

    uvicorn src.main:app --reload


## Usage

Send a text file as POST request to localhost:8000/upload/

    curl --request POST \
      --url http://localhost:8000/upload \
      --header 'Content-Type: multipart/form-data' \
      --form file=@~/rag_input.txt

It currently supports only raw text files.

## Troubleshooting

Libmagic issues when loading server documents

    brew install libmagic

Or use corresponding libraries on Linux/Windows.


Error stating averaged_perceptron_tagger is missing

    import nltk
    nltk.download('averaged_perceptron_tagger')
