# RAG-QA-Bot  
> “Knowledge is power. Let the system fetch it, you decide what to do with it.”  

An advanced Retrieval-Augmented Generation (RAG) style question-answering bot built using the LangChain framework. It allows you to load arbitrary document collections and ask questions of them — the system retrieves relevant context and then generates responses.  

---

## 🚀 Project Overview  
In today’s information-rich world, leveraging domain documents (PDFs, text, Markdown, etc.) to build conversational AI systems is no longer optional — it’s mandatory. This project demonstrates a robust end-to-end RAG architecture: document ingestion → vectorization → retrieval → generation.

## RAG-QA-Bot
> Knowledge-first question answering powered by LangChain, embeddings and a vector store.

One-line elevator pitch: build a searchable knowledge base from documents (PDF/MD/TXT) and ask natural language questions — the system retrieves relevant passages and generates grounded answers using an LLM.

Why this project exists
- Demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline.
- Practical for domain-specific assistants (docs, manuals, internal knowledge).
- Designed to be extended and dropped into a portfolio as a demonstrable, runnable project.

Highlights
- Plug-and-play document ingestion and chunking pipeline.
- Embeddings + vector store integration for semantic search.
- Retrieval chain that conditions an LLM on evidence before answering.
- CLI and optional Gradio UI (`app_Gradio.py`) for demos.
- Configurable via `params.yaml`.

Is this portfolio-worthy? Short answer: yes — with a few extras (demo video/GIF, screenshots, pinned deps, Docker, and a public demo) this is a strong portfolio piece. Read the "Portfolio tips" section below for specific, high-impact improvements.

## Quick demo (what reviewers want to see)
- Short animated GIF showing: 1) uploading documents, 2) building the index, 3) asking a question and receiving a grounded answer. 
- A short video (30–90s) explaining architecture and a sample query.

## Quickstart (Windows)
These commands assume PowerShell on Windows and the repository root is `c:\Campusx\langchain-QA-Bot`.

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure environment variables

Create a file named `.env` or export the required keys in your shell. Typical variables:

- OPENAI_API_KEY (or keys for whichever LLM/embedding provider you choose)
- OTHER_API_KEY

Keep secrets out of source control. Add `.env` to `.gitignore`.

4. Run the app (CLI)

```powershell
python app.py
```

5. Optional: Run the Gradio UI

```powershell
python app_Gradio.py
```

## Configuration
- `params.yaml` contains model names, embedding parameters, chunk size, top-k retrieval, and other runtime flags. Edit to match your desired LLM provider and resource constraints.

## Typical workflow
1. Put documents in the `data/` folder or use the loaders in `src/preprocessing/document_loader.py`.
2. Run the ingestion pipeline which will chunk, embed, and persist vectors via `src/preprocessing/vector_store.py`.
3. Ask questions using the CLI or Gradio UI. The retrieval chain (`core/retriever.py` and `core/QA_chain.py`) collects relevant context and calls the LLM to produce answers.

## Example queries and expected behavior
- "What are the main steps to set up the project?" → Should return a short, ordered list referencing the README or config.
- "Which file defines the retriever logic?" → Should point to `core/retriever.py` and include a short explanation.

## Project structure

Top-level files
- `app.py` — CLI entrypoint for interaction.
- `app_Gradio.py` — optional Gradio demo UI.
- `params.yaml` — runtime configuration.
- `requirements.txt` — Python dependencies (pin versions before publishing to portfolio).

Source code
- `core/QA_chain.py` — orchestration of retrieval + generation.
- `core/retriever.py` — retrieval wrapper over the vector store.

Preprocessing
- `src/preprocessing/document_loader.py` — helpers to load PDF/Markdown/TXT files.
- `src/preprocessing/doc_splitter.py` — chunking logic.
- `src/preprocessing/vector_store.py` — abstraction over the vector index.

Data
- `data/` — place your documents here for ingestion.

Notebooks
- `notebook/Experiment.ipynb` — used for experimentation and to verify embeddings/retrieval behavior.

## Security, costs, and notes
- The project may call external LLM/embedding APIs — be mindful of API costs.
- Do not check API keys into Git. Use `.env` or secure secret managers.

## Portfolio tips (high-impact, short checklist)
1. Add a short demo GIF (≤15s) and a 30–90s video in the repo (or a link to a hosted demo).
2. Pin dependency versions in `requirements.txt` and add a `requirements-freeze.txt` made with `pip freeze`.
3. Add a `Dockerfile` and a minimal `docker-compose.yml` for a reproducible demo environment.
4. Add a `README` section with example screenshots and a short script of the demo steps.
5. Add simple unit tests for critical modules (e.g., chunking, embedding wrapper, retriever logic) and run them in CI (GitHub Actions).
6. Add badges (build/test/pypi or Python version) and a short `CHANGELOG.md`.
7. Provide a live demo (Heroku, Render, Railway, or GitHub Pages linking to a recorded video) if possible.

## How to extend
- Swap the embedding or LLM provider by editing `params.yaml` and the provider wrapper in `src/models/`.
- Add alternative vector stores (FAISS, Chroma, Milvus) by implementing the store interface in `src/preprocessing/vector_store.py`.
