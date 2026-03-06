"""Simple querying interface to ask questions about sales."""
import argparse
from agents.rag import RAG


def main():
    parser = argparse.ArgumentParser(description='Query the sales RAG system')
    parser.add_argument('--question', required=True, help='Natural language question')
    args = parser.parse_args()

    rag = RAG()
    answer = rag.ask(args.question)
    print('Answer:')
    print(answer)


if __name__ == '__main__':
    main()