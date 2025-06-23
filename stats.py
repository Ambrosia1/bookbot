def get_word_count(text):
    words = text.split()
    return len(words)

def counting_characters(book_string):
    letter_count = {}
    lowercase_str = book_string.lower()
    for letter in lowercase_str:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def get_sort_characters(characters):
    dict_to_list = []
    for char in characters:
        if char.isalpha():
            char_list = characters[char]
            dict1 = {"char": char, "num": char_list}
            dict_to_list.append(dict1)
    dict_to_list.sort(reverse=True, key=sort_on)
    return dict_to_list

def sort_on(char_dict):
    return char_dict["num"]