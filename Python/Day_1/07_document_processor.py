documents = [
    {
        "title": "Introduction to RAG",
        "content": "RAG combines retrieval and generation."
    },
    {
        "title": "Python Basics",
        "content": "Python is a programming language."
    },
    {
        "title": "RAG Retrieval",
        "content": "A retriever finds relevant information."
    }
]


def check_document(document):
    if "RAG" in document["title"]:
        return True
    else:
        return False


for document in documents:
    if check_document(document):
        print("RAG document found:", document["title"])