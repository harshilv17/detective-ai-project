# Detective RAG

A simple Retrieval-Augmented Generation system that answers questions about a cold case using evidence files.

## How It Works

1. **loader.py** — Reads `.txt` evidence files from the `data/` folder
2. **vector.py** — Converts documents into embeddings using `sentence-transformers` and stores them in a FAISS index for similarity search
3. **rag.py** — Retrieves relevant documents for a query and builds a grounded answer with source citations (no LLM needed)

## Run

```bash
python3 rag.py
```

You'll be prompted to enter a question. The system retrieves the most relevant evidence and returns an answer with source citations.

## Evidence Files

The `data/` folder contains case evidence:

- `policelog.txt` — Police incident log
- `forensicsreport.txt` — Forensics analysis report
- `signalanalysis.txt` — Signal/frequency analysis
- `witnessrahul.txt` — Witness statement (Rahul)
- `witnesschestha.txt` — Witness statement (Chestha)

## Tech Stack

- Python
- sentence-transformers (`all-MiniLM-L6-v2`)
- FAISS (vector similarity search)
- NumPy
