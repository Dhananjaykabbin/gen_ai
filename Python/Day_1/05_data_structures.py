print("===== GENAI LEARNING PROFILE =====")

name = "Dhananjay"
age = 22
is_student = True
goal = "Generative AI Engineer"

skills = [
    "Python",
    "Prompt Engineering",
    "Machine Learning"
]

profile = {
    "name": name,
    "age": age,
    "goal": goal,
    "skills": skills
}

print("\nName:", profile["name"])
print("Age:", profile["age"])
print("Goal:", profile["goal"])
print("Skills:", profile["skills"])

print("\nNumber of skills:", len(profile["skills"]))