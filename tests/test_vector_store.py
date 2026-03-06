import pytest

from agents.vector_store import VectorStore


class DummyConnError(Exception):
    pass


def test_vector_store_unavailable(monkeypatch):
    # simulate connection failure
    def fake_connect(*args, **kwargs):
        raise Exception("no milvus")

    monkeypatch.setattr("agents.vector_store.connections.connect", fake_connect)
    store = VectorStore()
    assert store.available is False
    assert store.search([0] * 384) == []
