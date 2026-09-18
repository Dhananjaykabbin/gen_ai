documents = [
    {
        "title": "Introduction to RAG",
        "content": "RAG combines information retrieval with language generation.",
        "source": "rag_intro.pdf"
    },
    {
        "title": "RAG Retrieval",
        "content": "A retriever searches a knowledge base for relevant information.",
        "source": "retrieval.pdf"
    },
    {
        "title": "RAG Generation",
        "content": "The retrieved information is provided to an LLM to generate an answer.",
        "source": "generation.pdf"
    }
]

print("Number of documents:", len(documents))

print("\nFirst document:")
print(documents[0])

print("\nFirst document title:")
print(documents[0]["title"])

print("\nFirst document content:")
print(documents[0]["content"])

print("\nFirst document source:")
print(documents[0]["source"])