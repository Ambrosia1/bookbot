from stats import get_word_count
from stats import counting_characters
from stats import get_sort_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    sorted_chars = get_sort_characters(counting_characters(text))
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()