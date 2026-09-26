def clean_text(text):
    return text.strip().lower()


def count_words(text):
    return len(text.split())