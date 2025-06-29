from stats import get_word_count
from stats import counting_characters
from stats import get_sort_characters
import sys

def main():
    sys_list = len(sys.argv)
    if sys_list != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
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