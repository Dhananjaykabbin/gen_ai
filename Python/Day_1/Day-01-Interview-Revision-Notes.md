# GenAI Engineering Journey — Interview Revision Notes

## Day 1 — Python Foundations

> **Goal:** Build strong Python fundamentals specifically for Generative AI engineering and interviews.

---

# 1. Variables

## Definition

A **variable** is a name used to refer to a value/object in a Python program.

```python
name = "Dhananjay"
age = 22
```

- `name`, `age` → variables
- `"Dhananjay"`, `22` → values
- `=` → assignment operator

### 🔥 MUST KNOW
Python variables do not require explicit type declarations.

Python is **dynamically typed**: the type is associated with the value/object, and a variable can refer to values of different types at different times.

### ⭐ Interview Questions

**Q1. What is a variable in Python?**  
A: A variable is a name used to refer to a value/object.

**Q2. What is the assignment operator?**  
A: `=` is the assignment operator; it assigns a value to a variable.

**Q3. Is Python statically or dynamically typed?**  
A: Python is dynamically typed.

---

# 2. Data Types

A **data type** identifies the kind of value an object represents.

## Important built-in types

| Type | Example |
|---|---|
| `str` | `"RAG"` |
| `int` | `22` |
| `float` | `7.73` |
| `bool` | `True` |
| `list` | `["RAG", "LLM"]` |
| `tuple` | `("RAG", "LLM")` |
| `set` | `{"RAG", "LLM"}` |
| `dict` | `{"topic": "RAG"}` |
| `NoneType` | `None` |

Use `type()` to inspect a value's type:

```python
print(type("RAG"))
print(type(22))
```

### Boolean

```python
is_student = True
has_job = False
```

Only `True` and `False` are Boolean values.

### None

`None` represents the absence of a value.

```python
response = None
```

### ⭐ Interview Questions

**Q1. Name common built-in Python data types.**  
A: `str`, `int`, `float`, `bool`, `list`, `tuple`, `set`, `dict`, and `NoneType`.

**Q2. What is `None`?**  
A: `None` is a special singleton object representing the absence of a value.

**Q3. What is the difference between `True` and `"True"`?**  
A: `True` is a Boolean; `"True"` is a string.

---

# 3. `input()`

`input()` is a built-in function used to receive input from the user.

```python
name = input("Enter your name: ")
```

If the user enters `22`, the returned value is:

```python
"22"
```

not the integer `22`.

### 🔥 MUST KNOW

**`input()` always returns a string.**

### ⭐ Interview Question

**Q. What is the return type of `input()`?**  
A: `input()` returns the user's input as a string.

---

# 4. Functions

A **function** is a reusable block of code designed to perform a particular task.

Built-in examples:

```python
print()
input()
type()
len()
```

A function can also be created using `def`:

```python
def greet():
    print("Hello")
```

Calling it:

```python
greet()
```

### Terminology

- `def` → keyword used to define a function
- `greet` → function name
- function call → `greet()`
- parameter → variable in the function definition
- argument → actual value passed to a function

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

Here:
- `a`, `b` → parameters
- `10`, `20` → arguments
- `return` → sends the result back to the caller

### `print()` vs `return`

```python
def add(a, b):
    print(a + b)
```

`print()` displays a value.

```python
def add(a, b):
    return a + b
```

`return` sends a value back to the caller so it can be stored or used.

### 🔥 MUST KNOW

Parameter vs argument and `print()` vs `return` are common interview topics.

### ⭐ Interview Questions

**Q1. What is a function?**  
A: A reusable block of code designed to perform a specific task.

**Q2. What is a parameter?**  
A: A variable defined in a function definition.

**Q3. What is an argument?**  
A: An actual value supplied during a function call.

**Q4. Difference between parameter and argument?**  
A: Parameters appear in the function definition; arguments are supplied when calling the function.

**Q5. Difference between `print()` and `return`?**  
A: `print()` displays a value; `return` sends a value back to the caller.

---

# 5. f-Strings

An **f-string** is a formatted string literal that allows expressions to be embedded inside a string.

```python
name = "Dhananjay"
message = f"Hello {name}"
```

Output:

```text
Hello Dhananjay
```

### 🚀 GenAI Connection

f-strings are useful for **dynamic prompt construction**:

```python
topic = "RAG"

prompt = f"""
Explain {topic} in simple words.
Give a real-world example.
"""
```

The value of `topic` is inserted into the prompt.

### ⭐ Interview Question

**Q. What is an f-string?**  
A: An f-string is a formatted string literal that allows expressions to be embedded inside a string using `{}`.

---

# 6. Strings

A **string** is a sequence of characters.

```python
text = "Generative AI"
```

## Indexing

```python
text = "RAG"

print(text[0])
```

Output:

```text
R
```

Python uses **zero-based indexing**.

```text
R → index 0
A → index 1
G → index 2
```

## Slicing

```python
text = "Generative AI"
print(text[0:10])
```

The syntax is:

```python
text[start:stop]
```

The `stop` index is excluded.

## Common string methods

```python
text.strip()      # removes surrounding whitespace
text.lower()      # converts to lowercase
text.upper()      # converts to uppercase
text.replace()    # replaces text
text.split()      # splits string into a list
```

Example:

```python
text = "Python RAG LLM"
words = text.split()
```

Result:

```python
["Python", "RAG", "LLM"]
```

### 🔥 MUST KNOW

Strings are **immutable**.

### 🚀 GenAI Connection

Strings are fundamental to GenAI because prompts, user queries, document text, instructions, and model responses are commonly represented as text.

### ⭐ Interview Questions

**Q1. What is a string?**  
A: A sequence of characters represented by the `str` type.

**Q2. Are strings mutable?**  
A: No. Strings are immutable.

**Q3. What does `split()` do?**  
A: It splits a string into a list of substrings.

**Q4. What does `strip()` do?**  
A: It removes leading and trailing whitespace by default.

---

# 7. Type Conversion / Type Casting

**Type conversion** means converting a value from one data type to another.

```python
age = "22"
age = int(age)
```

Common conversion functions:

```python
int()
float()
str()
bool()
```

Example:

```python
age = int(input("Enter age: "))
```

Flow:

```text
user input
    ↓
"22"          string
    ↓
int()
    ↓
22            integer
```

### 🔥 MUST KNOW

`input()` returns a string, so conversion is often necessary when numerical input is required.

### ⭐ Interview Question

**Q. Why would you use `int(input(...))`?**  
A: Because `input()` returns a string, and `int()` converts that string into an integer.

---

# 8. Operators

Operators perform operations on values.

## Arithmetic operators

```text
+   addition
-   subtraction
*   multiplication
/   division
//  floor division
%   modulus/remainder
**  exponentiation
```

Example:

```python
10 % 3
```

Result:

```text
1
```

## Comparison operators

```text
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
```

Comparison expressions produce Boolean values.

```python
10 > 5
```

Result:

```text
True
```

### 🔥 `=` vs `==`

```python
x = 10
```

`=` → assignment

```python
x == 10
```

`==` → equality comparison

### Logical operators

```text
and
or
not
```

### ⭐ Interview Questions

**Q1. Difference between `=` and `==`?**  
A: `=` assigns a value; `==` compares two values for equality.

**Q2. What does `%` do?**  
A: It returns the remainder of a division.

**Q3. What is the difference between `/` and `//`?**  
A: `/` performs division and produces a floating-point result; `//` performs floor division.

---

# 9. Lists

A **list** stores multiple values in an ordered collection.

```python
skills = ["Python", "RAG", "Prompt Engineering"]
```

Indexing:

```python
skills[0]
```

returns:

```text
Python
```

Python lists use zero-based indexing.

## Common operations

```python
len(skills)
skills.append("Agents")
skills.remove("RAG")
skills[0] = "Advanced Python"
```

### 🔥 MUST KNOW

Lists are **mutable**.

### Nested list

Lists can contain dictionaries or other lists:

```python
documents = [
    {"title": "RAG", "source": "rag.pdf"},
    {"title": "LLM", "source": "llm.pdf"}
]
```

### 🚀 GenAI Connection

Lists commonly represent:

- retrieved documents
- search results
- messages
- chunks
- model outputs
- datasets

### ⭐ Interview Questions

**Q1. Is a list mutable?**  
A: Yes.

**Q2. What is zero-based indexing?**  
A: The first element is accessed using index `0`.

**Q3. What does `len()` return?**  
A: The number of elements in a collection or characters in a string.

---

# 10. Dictionaries

A **dictionary** is a mutable collection of **key-value pairs**.

```python
student = {
    "name": "Dhananjay",
    "age": 22,
    "goal": "Generative AI Engineer"
}
```

Terminology:

```text
"name"                → key
"Dhananjay"           → value
```

Access:

```python
student["name"]
```

Add/update:

```python
student["skills"] = ["Python", "RAG"]
```

Useful methods:

```python
student.keys()
student.values()
student.items()
student.get("email")
```

### `.get()`

```python
student.get("email")
```

returns `None` if the key does not exist by default, instead of raising a `KeyError`.

A default can also be supplied:

```python
student.get("email", "Not available")
```

### 🚀 GenAI Connection

Dictionaries are heavily used for:

- API requests
- API responses
- configuration
- metadata
- structured model output
- document information

### ⭐ Interview Questions

**Q1. What is a dictionary?**  
A: A mutable collection of key-value pairs.

**Q2. What is a key-value pair?**  
A: A key identifies/accesses an associated value.

**Q3. Why use `.get()` instead of `dict[key]`?**  
A: `.get()` can safely return a default value when the key is absent instead of raising `KeyError`.

---

# 11. Mutable vs Immutable

**Mutable** means an object can be changed after creation.

**Immutable** means an object cannot be changed after creation.

### Common examples

```text
Mutable:
list
dict
set

Immutable:
str
int
float
bool
tuple
```

### ⭐ Interview Question

**Q. What is the difference between mutable and immutable objects?**  
A: Mutable objects can be modified after creation; immutable objects cannot be modified after creation.

---

# 12. Nested Data Structures

A data structure can contain another data structure.

Example:

```python
profile = {
    "name": "Dhananjay",
    "skills": [
        "Python",
        "Prompt Engineering",
        "RAG"
    ]
}
```

Here:

```text
profile → dictionary
skills  → list inside the dictionary
```

Access:

```python
profile["skills"][0]
```

This means:

1. Get `"skills"` from the dictionary.
2. Get index `0` from the resulting list.

### 🚀 GenAI Connection

Real API responses and RAG data frequently contain nested lists and dictionaries.

---

# 13. Conditions

Conditions allow a program to make decisions.

```python
age = 22

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Multiple conditions:

```python
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

### 🔥 Indentation

Python uses indentation to define code blocks.

```python
if age >= 18:
    print("Adult")
```

### 🚀 GenAI Connection

Conditions are used for:

- input validation
- checking whether documents exist
- handling failed searches
- deciding which AI workflow to execute
- routing user requests

### ⭐ Interview Questions

**Q1. What is an `if` statement?**  
A: It executes a block of code when a condition evaluates to true.

**Q2. Difference between `if`, `elif`, and `else`?**  
A: `if` checks the first condition, `elif` checks additional conditions, and `else` executes when none of the preceding conditions are true.

**Q3. Why is indentation important in Python?**  
A: Python uses indentation to define code blocks.

---

# 14. Loops

A loop repeats a block of code.

## `for` loop

```python
topics = ["Python", "RAG", "LLM"]

for topic in topics:
    print(topic)
```

The loop processes each element.

An **iteration** is one pass through the loop.

## `range()`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The stop value is excluded.

## `while`

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

A `while` loop continues while its condition is true.

## `break`

Exits the loop completely.

## `continue`

Skips the current iteration and moves to the next iteration.

### 🔥 MUST KNOW

```text
break     → exit loop
continue  → skip current iteration
```

### 🚀 GenAI Connection

Loops are useful for:

- processing multiple documents
- processing chunks
- evaluating multiple prompts
- batch processing
- handling search results

### ⭐ Interview Questions

**Q1. What is a loop?**  
A: A control structure that repeatedly executes a block of code.

**Q2. Difference between `for` and `while`?**  
A: `for` is commonly used to iterate over an iterable; `while` repeats while a condition remains true.

**Q3. What is an iteration?**  
A: One execution/pass through a loop.

**Q4. What is an infinite loop?**  
A: A loop that continues indefinitely because its termination condition is never reached.

**Q5. Difference between `break` and `continue`?**  
A: `break` terminates the loop; `continue` skips the current iteration.

---

# 15. Functions — Practical AI Pattern

Functions allow us to organize AI application logic.

```python
def generate_prompt(topic):
    prompt = f"""
    Explain {topic}.
    Give a simple example.
    """
    return prompt
```

Then:

```python
prompt = generate_prompt("RAG")
```

This creates reusable logic.

### 🚀 GenAI Connection

A real application may contain functions such as:

```python
def retrieve_documents(query):
    ...

def build_prompt(query, documents):
    ...

def generate_answer(prompt):
    ...
```

These functions can become separate stages of a GenAI pipeline.

---

# 16. List Comprehensions

A **list comprehension** is a concise way to create a list.

Traditional:

```python
squares = []

for number in numbers:
    squares.append(number * number)
```

List comprehension:

```python
squares = [number * number for number in numbers]
```

With a condition:

```python
even_numbers = [
    number for number in numbers
    if number % 2 == 0
]
```

### 🚀 GenAI Connection

Useful when transforming collections of:

- documents
- chunks
- search results
- model outputs

### ⭐ Interview Question

**Q. What is a list comprehension?**  
A: A concise Python syntax for creating a list by applying an expression to elements of an iterable, optionally with a condition.

---

# 17. JSON

## Definition

**JSON = JavaScript Object Notation**

JSON is a lightweight text format used to represent and exchange structured data.

Example:

```json
{
    "name": "Dhananjay",
    "goal": "Generative AI Engineer",
    "skills": [
        "Python",
        "RAG"
    ]
}
```

### Python dictionary vs JSON

Python:

```python
data = {
    "name": "Dhananjay"
}
```

JSON:

```json
{
    "name": "Dhananjay"
}
```

A Python dictionary is a Python object. JSON is a data representation/text format.

---

# 18. Python ↔ JSON

Import the JSON module:

```python
import json
```

## Python → JSON

```python
json_data = json.dumps(data)
```

`json.dumps()` serializes a Python object into a JSON-formatted string.

## JSON → Python

```python
data = json.loads(json_data)
```

`json.loads()` parses a JSON-formatted string into a Python object.

### 🔥 MUST KNOW

```text
dumps → Python object → JSON string
loads  → JSON string → Python object
```

### `indent=4`

```python
json.dumps(data, indent=4)
```

`indent=4` only makes JSON more readable by formatting it with indentation. It does not change the underlying data.

### 🚀 GENAI CONNECTION

A typical API communication flow is conceptually:

```text
Python application
      ↓
HTTP request
      ↓
JSON
      ↓
LLM API
      ↓
JSON response
      ↓
Python application
```

Understanding JSON is essential for API-based GenAI development.

### ⭐ Interview Questions

**Q1. What is JSON?**  
A: JSON is a lightweight text format used to represent and exchange structured data.

**Q2. Difference between a Python dictionary and JSON?**  
A: A dictionary is a Python object/data structure; JSON is a text-based data interchange format.

**Q3. Difference between `json.dumps()` and `json.loads()`?**  
A: `dumps()` serializes a Python object to a JSON-formatted string; `loads()` parses a JSON string into a Python object.

**Q4. Does `indent=4` change JSON data?**  
A: No. It only formats the JSON for readability.

---

# 19. Important GenAI Mental Model

The Python concepts learned so far connect to GenAI like this:

```text
USER QUERY
    ↓
String
    ↓
Python variable
    ↓
Dictionary / JSON
    ↓
API request
    ↓
LLM
    ↓
JSON response
    ↓
Dictionary / List
    ↓
Python processing
    ↓
Final answer
```

For RAG:

```text
User Question
      ↓
String
      ↓
Retrieve documents
      ↓
List of documents
      ↓
Dictionary metadata
      ↓
Loop / processing
      ↓
Prompt construction
      ↓
LLM API
      ↓
Response
```

---

# 20. Day 1 Interview Quick Revision

Before an interview, make sure you can explain:

- Variable
- Dynamic typing
- Data type
- `str`, `int`, `float`, `bool`
- `None`
- `input()`
- Function
- Parameter vs argument
- `return` vs `print()`
- f-string
- String indexing and slicing
- String immutability
- Type conversion
- Arithmetic/comparison/logical operators
- `=` vs `==`
- List
- Zero-based indexing
- List mutability
- Dictionary
- Key-value pair
- `.get()`
- Nested data structures
- Condition
- Indentation
- `for` loop
- `while` loop
- Iteration
- `range()`
- `break`
- `continue`
- Function reuse
- List comprehension
- JSON
- Python dictionary vs JSON
- `json.dumps()`
- `json.loads()`

---

# Day 1 Practical Files

```text
Day-01-Python/
│
├── 01_basics.py
├── 02_prompt_generator.py
├── 03_prompt_builder.py
├── 04_variables_test.py
├── 05_data_structures.py
├── 06_rag_data.py
├── 07_document_processor.py
├── 08_ai_document_filter.py
└── 09_json_genai.py
```

These demonstrate your progression from Python basics toward GenAI-oriented programming.

---

# Day 1 GitHub Documentation

For GitHub, your daily README can eventually contain:

```markdown
# Day 1 — Python Foundations for GenAI

## Concepts Learned

- Variables and dynamic typing
- Python data types
- User input
- Functions
- Parameters and arguments
- f-strings
- Strings and string methods
- Type conversion
- Operators
- Lists
- Dictionaries
- Nested data structures
- Conditions
- Loops
- List comprehensions
- JSON
- Python ↔ JSON conversion

## Practical Work

Built small Python programs for:

- Prompt generation
- GenAI learning profile
- Document processing
- AI document filtering
- JSON data handling

## GenAI Connection

Learned how Python variables, lists, dictionaries, strings, and JSON form the foundation for:

- Prompt construction
- Document processing
- API communication
- RAG pipelines
- LLM applications

## Interview Preparation

Prepared interview questions covering Python fundamentals, data structures, functions, loops, conditions, mutability, and JSON.

## Day 1 Outcome

Built a foundation for moving from Python programming to API-based Generative AI development.
```
