def test_rag_llm_unreachable(monkeypatch):
    from agents.rag import RAG
    # force a bad URL
    r = RAG(llm_url="http://localhost:59999")
    res = r.ask("hello")
    assert "generated_text" in res
