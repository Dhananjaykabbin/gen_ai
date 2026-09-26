from utils.text_utils import clean_text, count_words

text = "  Generative AI is powerful  "

cleaned = clean_text(text)
words = count_words(cleaned)

print("Cleaned Text:", cleaned)
print("Word Count:", words)