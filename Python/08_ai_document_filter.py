documents = [
    {"title": "RAG Introduction", "type": "AI"},
    {"title": "Python Basics", "type": "Programming"},
    {"title": "LLM Fundamentals", "type": "AI"},
    {"title": "Database Basics", "type": "Database"},
    {"title": "RAG Advanced Techniques", "type": "AI"}
]

def is_ai_document(document):
    if "AI" in document["type"]:
        return True
    else:
        return False

for document in documents:
    if is_ai_document(document):
        print(document["title"])