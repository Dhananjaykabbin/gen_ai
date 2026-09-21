#import os

with open("rag_description.txt", "w") as file:
    file.write("RAG stands for Retrieval-Augmented Generation.\n")
    file.write("RAG retrieves relevant information from documents before generating an answer.\n")

with open("rag_description.txt", "r") as file:
    RAG=file.read()

print(RAG)