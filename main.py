def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    

    char_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_counts:
                char_counts[char] +=1
            else:
                char_counts[char] = 1

    #print(char_counts)

    list_of_dicts = []
    for char in char_counts:
        list_of_dicts.append({"char": char, "num": char_counts[char]})
    list_of_dicts.sort(reverse=True,key=sort_on)
    print(list_of_dicts)


def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    text_dict = {}
    for i in text:
        i_low = i.lower()
        if i_low in text_dict:
            text_dict[i_low] += 1
        else: text_dict[i_low] = 1
    return text_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()