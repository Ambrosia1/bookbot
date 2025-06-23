from stats import get_word_count
from stats import counting_characters
from stats import get_sort_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
    print(counting_characters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()