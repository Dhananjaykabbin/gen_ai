import json

profile = {
    "name": "Dhananjay",
    "role": "AI/ML Student",
    "goal": "Generative AI Engineer",
    "skills": [
        "Python",
        "Prompt Engineering",
        "RAG"
    ]
}

print("Python Dictionary:")
print(profile)

json_data = json.dumps(profile, indent=4)

print("\nJSON:")
print(json_data)

converted_data = json.loads(json_data)

print("\nConverted back to Python:")
print(converted_data)

print("\nGoal:")
print(converted_data["goal"])