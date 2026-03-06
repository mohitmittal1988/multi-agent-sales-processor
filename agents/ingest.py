"""Ingestion script for sales files."""
import argparse
import csv
import json
from agents.vector_store import VectorStore


def load_file(path):
    if path.lower().endswith('.csv'):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    elif path.lower().endswith('.json'):
        with open(path) as f:
            return json.load(f)
    else:
        raise ValueError('Unsupported file type')


def main():
    parser = argparse.ArgumentParser(description='Ingest sales file into vector store')
    parser.add_argument('--file', required=True, help='Path to input file')
    args = parser.parse_args()

    data = load_file(args.file)
    texts = []
    meta = []
    for record in data:
        text = json.dumps(record)
        texts.append(text)
        meta.append(record)

    # embed
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts, show_progress_bar=True)

    store = VectorStore()
    store.add_records(embeddings, texts, meta)
    print(f'Indexed {len(texts)} records')


if __name__ == '__main__':
    main()