"""Simple MCP server exposing endpoints for agent coordination."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agents.agent import ClaudeAgent, SalesAnalyzer

app = FastAPI(title='Multi-agent MCP')

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class Request(BaseModel):
    query: str

@app.post('/process')
def process(req: Request):
    agent_chain = ClaudeAgent([SalesAnalyzer()])
    result = agent_chain.run(req.query)
    return {'result': result}

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/')
def root():
    return {"message": "Go to /static/index.html for the web interface"}