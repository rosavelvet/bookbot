from stats import (
    get_word_count,
    get_char_count,
    sort_dictionary
)
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    words_count = get_word_count(text)
    chars_dict = get_char_count(text)
    chars_sorted_list = sort_dictionary(chars_dict)
    print("=========BOOKBOT=========")
    print("-----------Word Count-----------")
    print(f"Found {words_count} total words")
    print("-----------Character Count------")
    for d in chars_sorted_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()