from stats import (
    get_word_count,
    get_char_count,
    sort_dictionary
)


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_word_count(text)
    chars_sorted_list = sort_dictionary(get_char_count(text))
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