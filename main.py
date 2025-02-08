def count_words(text):
    return len(text.split())


def count_characters(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(dict):
    return dict["num"]


def print_report(char_dict):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_dict_list = [
        {"name": k, "num": char_dict[k]} for k in char_dict if k in alphabet
    ]
    char_dict_list.sort(reverse=True, key=sort_on)

    for entry in char_dict_list:
        print(f"The '{entry['name']}' character was found {entry['num']} times")


def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    n_words = count_words(text)
    char_dict = count_characters(text)

    print_report(char_dict)


if __name__ == "__main__":
    main()
