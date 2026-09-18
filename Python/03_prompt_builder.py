print("===== GENAI PROMPT BUILDER =====")

name = input("Enter your name: ")
topic = input("What topic do you want to learn? ")
level = input("What is your level? (beginner/intermediate/advanced): ")

prompt = f"""
You are an expert AI teacher.

Student name: {name}
Student level: {level}
Topic: {topic}

Explain the topic clearly.

Include:
1. Simple definition
2. Technical explanation
3. Real-world example
4. Advantages
5. Limitations
6. Interview questions
7. Practical coding example
"""

print("\n===== GENERATED PROMPT =====")
print(prompt)