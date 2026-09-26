def create_prompt(topic, level):
    return f"Explain {topic} for a {level} learner."


prompt1 = create_prompt("RAG", "beginner")
prompt2 = create_prompt("LLM", "intermediate")

print(prompt1)
print(prompt2)