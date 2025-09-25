def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
            continue
        chars[lowered] = 1
    return chars


def sort_dictionary(dictionary):
    sorted_list = []
    for c in dictionary:
        sorted_list.append({"char": c, "num": dictionary[c]})
    sorted_list.sort(key=get_num_char, reverse=True)
    return sorted_list


def get_num_char(dictionary):
    return dictionary["num"]