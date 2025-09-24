def get_word_count(book):
    words = book.split()
    return len(words)


def get_symbol_count(book):
    symbols = {}
    for symbol in book:
        low_symbol = symbol.lower()
        if low_symbol in symbols:
            symbols[low_symbol] += 1
            continue
        symbols[low_symbol] = 1
    return symbols