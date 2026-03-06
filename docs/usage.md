# Usage

## Prerequisites

- Docker & Docker Compose
- Python 3.11 (for running scripts/tests locally)

## Quick start (Docker Compose)

1. Build and start all services:

   ```sh
   docker-compose up --build
   ```

2. Ingest sample data (inside the `mcp` container or locally):

   ```sh
   python agents/ingest.py --file data/sample_sales.csv
   ```

3. Query via CLI:

   ```sh
   python agents/query.py --question "What were last month's total sales?"
   ```

4. Browse the web UI:
   - static HTML: http://localhost:8000/static/index.html
   - Streamlit: http://localhost:8501

5. Health check:

   ```sh
   curl http://localhost:8000/health
   ```


## Running tests

Activate a virtualenv and install requirements, then:

```sh
pytest
```


## Environment variables

Copy `.env.example` and edit values as needed:

```
MILVUS_HOST=milvus
MILVUS_PORT=19530
LLM_URL=http://llm:8080/generate
```
