from stats import get_word_count
from stats import get_symbol_count


def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {get_word_count(text)} total words")
    print(get_symbol_count(text))


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()