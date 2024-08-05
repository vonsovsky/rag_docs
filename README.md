# rag_docs

## Installation

Install requirements

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Set up OPENAI_API_KEY environment variable

    export set up OPENAI_API_KEY=sk-****

Run FastAPI server

    uvicorn src.main:app --reload


## Usage

Send file to POST url localhost:8000/

## Troubleshooting

Libmagic issues when loading server documents

    brew install libmagic

Or use corresponding libraries on Linux/Windows.


Error stating averaged_perceptron_tagger is missing

    import nltk
    nltk.download('averaged_perceptron_tagger')
