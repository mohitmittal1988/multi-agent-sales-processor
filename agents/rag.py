"""Retrieval-Augmented Generation coordination."""
from agents.vector_store import VectorStore
import requests
from sentence_transformers import SentenceTransformer
import os


class RAG:
    def __init__(self, llm_url=None):
        self.store = VectorStore()
        self.embed_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.llm_url = llm_url or os.getenv('LLM_URL', 'http://llm:8080/generate')

    def ask(self, question):
        try:
            q_emb = self.embed_model.encode([question])
            docs = self.store.search(q_emb, top_k=5)
            prompt = self._build_prompt(question, docs)
            
            try:
                resp = requests.post(self.llm_url, json={'inputs': prompt}, timeout=10)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:
                print(f"LLM error: {e}, returning basic response")
                return {'generated_text': f"Based on query '{question}': Unable to reach LLM. Try again later."}
        except Exception as e:
            print(f"RAG error: {e}")
            return {'generated_text': f"Error processing query: {str(e)}"}

    def _build_prompt(self, question, docs):
        context = "\n".join(docs) if docs else "No relevant documents found."
        return f"Use the context from sales records:\n{context}\n\nQ: {question}\nA:"