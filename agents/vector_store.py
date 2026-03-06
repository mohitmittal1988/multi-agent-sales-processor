"""Wrapper around Milvus vector database."""
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
import os


class VectorStore:
    def __init__(self, collection_name='sales'):
        host = os.getenv('MILVUS_HOST', 'milvus')
        port = int(os.getenv('MILVUS_PORT', '19530'))
        try:
            connections.connect('default', host=host, port=port)
            self.collection_name = collection_name
            if not Collection.exists(self.collection_name):
                self._create_collection()
            self.collection = Collection(self.collection_name)
            self.available = True
        except Exception as e:
            print(f"Warning: Could not connect to Milvus: {e}")
            self.available = False
            self.collection = None

    def _create_collection(self):
        fields = [
            FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, dim=384),
            FieldSchema(name='text', dtype=DataType.VARCHAR, max_length=65535),
        ]
        schema = CollectionSchema(fields, description='sales records')
        Collection(self.collection_name, schema)

    def add_records(self, embeddings, texts, metadata=None):
        if not self.available:
            print("Vector store not available, skipping indexing")
            return
        # embeddings: list of lists
        # texts: list of strings
        self.collection.insert([embeddings, texts])
        self.collection.flush()

    def search(self, query_embeddings, top_k=5):
        if not self.available:
            print("Vector store not available, returning all texts")
            return []
        results = self.collection.search(
            query_embeddings,
            "embedding",
            params={"metric_type": "IP", "params": {"nprobe": 10}},
            limit=top_k,
            output_fields=["text"]
        )
        return [hit.entity.get('text') for hits in results for hit in hits]