# Architecture Overview

This repository implements a **multi-agent** retrieval-augmented generation (RAG) system for processing sales data. Key components:

1. **Agents** – Python classes under `agents/` that perform specific tasks:
   - `ingest.py` loads CSV/JSON sales records and indexes them in a vector store.
   - `vector_store.py` wraps a Milvus collection for storing and searching embeddings.
   - `rag.py` coordinates embedding the query, retrieving documents, and calling an LLM.
   - `claude_agent.py` illustrates a simple agent orchestrator with a `SalesAnalyzer`.
   - `query.py` and `ingest.py` provide CLI utilities.

2. **Vector database** – Milvus runs in Docker Compose (`docker-compose.yml`).
   Embeddings are computed with `sentence-transformers` (`all-MiniLM-L6-v2`).

3. **LLM** – an external text-generation inference service (container at `llm:8080`).
   The RAG component sends prompt + context to the LLM via HTTP.

4. **FastAPI MCP server** – `mcp_server.py` exposes `/process` and `/health` endpoints.
   Static UI files are served from `static/`.

5. **User interface** – a simple HTML page (`static/index.html`) and a Streamlit app
   (`streamlit_app.py`) for interacting with the system.

Everything is orchestrated with Docker Compose; see `docker-compose.yml` for services.

---

This monorepo is deliberately small; each piece can be replaced or upgraded independently.