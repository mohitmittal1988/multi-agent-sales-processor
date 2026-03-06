# Multi-Agent Sales Processor

A powerful multi-agent system that processes and analyzes sales data using RAG (Retrieval-Augmented Generation), vector databases, and large language models. Ask natural language questions about your sales data and get instant AI-powered answers.

## Features

- **AI-Powered Queries** - Ask questions in plain English, get intelligent answers
- **Vector Database** - Uses Milvus for fast semantic search
- **RAG System** - Combines data retrieval with LLM generation
- **Multi-Agent Architecture** - Specialized agents for different tasks
- **Web Interface** - Easy-to-use Streamlit dashboard
- **REST API** - FastAPI backend for integration
- **Docker Support** - Run everything in containers with docker-compose
- **Testing** - Full test suite included

## How It Works

```
User Question
    ↓
Vector Database (Embedding Search)
    ↓
Relevant Data Retrieved
    ↓
AI Agent (LLM Processing)
    ↓
Answer Returned
```

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI, MCP Server
- **Vector DB:** Milvus
- **Embeddings:** Sentence Transformers
- **LLM:** Claude (Anthropic)
- **Python:** 3.9+

## Project Structure

```
multi-agent-sales-processor/
├── agents/                 # AI agent logic
│   ├── agent.py           # Main agent orchestration
│   ├── query.py           # Query interface
│   ├── rag.py             # RAG system
│   ├── vector_store.py    # Vector database interaction
│   ├── ingest.py          # Data ingestion pipeline
│   └── __init__.py
├── data/                   # Sample data
│   └── sample_sales.csv   # Sales dataset
├── tests/                  # Unit tests
│   ├── test_ingest.py
│   ├── test_rag.py
│   ├── test_vector_store.py
│   └── test_mcp.py
├── docs/                   # Documentation
│   ├── architecture.md
│   └── usage.md
├── scripts/                # Utility scripts
│   └── run_demo.sh
├── static/                 # Web assets
│   └── index.html
├── mcp_server.py          # FastAPI server
├── streamlit_app.py       # Web UI
├── docker-compose.yml     # Docker setup
├── Dockerfile.mcp         # MCP container
├── Dockerfile.streamlit   # Streamlit container
├── requirements.txt       # Python dependencies
└── README.md

```

## Installation

### Prerequisites

- Python 3.9 or higher
- Docker & Docker Compose (optional)
- Git

### Option 1: Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohitmittal1988/multi-agent-sales-processor.git
   cd multi-agent-sales-processor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

### Option 2: Docker Installation

No installation needed! Just run:
```bash
docker-compose up
```

## Quick Start

### Using Docker (Recommended)

```bash
# Start all services
docker-compose up

# Open your browser
# Streamlit UI: http://localhost:8501
# API Health: http://localhost:9000/health
```

### Using Local Python

**Terminal 1 - Start the API:**
```bash
uvicorn mcp_server:app --host 0.0.0.0 --port 9000
```

**Terminal 2 - Start the Web UI:**
```bash
streamlit run streamlit_app.py
```

Then open: `http://localhost:8501`

## Usage

### Web Interface (Streamlit)

1. Open `http://localhost:8501`
2. Type your question in the text box
3. Click "Ask"
4. Get your answer!

**Example questions:**
- "What were total sales in Q1?"
- "Which product had the highest revenue?"
- "Show me sales by region"
- "What's the average order value?"

### REST API

**Process Query Endpoint:**

```bash
curl -X POST http://localhost:9000/process \
  -H "Content-Type: application/json" \
  -d '{"query": "What were total sales in Q1?"}'
```

**Response:**
```json
{
  "result": "Total sales in Q1 were $250,000..."
}
```

**Health Check:**
```bash
curl http://localhost:9000/health
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/process` | Process a sales query |
| GET | `/health` | Health check |
| GET | `/` | API welcome message |

## Configuration

### Environment Variables

Create `.env` file:

```env
# API Keys
ANTHROPIC_API_KEY=your_claude_api_key

# Database
MILVUS_HOST=localhost
MILVUS_PORT=19530

# Server
API_PORT=9000
API_HOST=0.0.0.0

# Data
DATA_PATH=data/sample_sales.csv
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=agents

# Run specific test
pytest tests/test_rag.py
```

## Performance

- **Query Processing:** 2-5 seconds per question
- **Vector Search:** <100ms for similarity matching
- **LLM Generation:** 1-3 seconds
- **Concurrent Users:** Supports 10+ simultaneous connections with Docker

## Troubleshooting

### Port Already in Use
```bash
# Change port in docker-compose.yml or:
docker-compose down
docker-compose up
```

### Out of Memory
```bash
# Increase Docker memory limit
# Edit docker-compose.yml
# services:
#   llm:
#     deploy:
#       resources:
#         limits:
#           memory: 8G
```

### No Results Found
- Make sure data is ingested: `python -m agents.ingest`
- Check vector database: `docker-compose logs milvus`
- Verify API key in `.env`

## Development

### Add New Agent

Create `agents/my_agent.py`:
```python
from agents.agent import BaseAgent

class MyAgent(BaseAgent):
    def process(self, data):
        # Your logic here
        return result
```

### Add Tests

Create `tests/test_my_feature.py`:
```python
import pytest
from agents.my_agent import MyAgent

def test_my_agent():
    agent = MyAgent()
    result = agent.process(data)
    assert result is not None
```

## Architecture

See [docs/architecture.md](docs/architecture.md) for detailed system design.

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- Open an issue on GitHub
- Check [docs/usage.md](docs/usage.md)
- Review test files for examples

## Roadmap

- [ ] Support for multiple LLM providers
- [ ] Advanced filtering and aggregation
- [ ] Real-time data ingestion
- [ ] Multi-language support
- [ ] Performance optimizations
- [ ] Kubernetes deployment

---

**Made with ❤️ by the Multi-Agent Team**
