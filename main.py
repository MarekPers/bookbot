def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    number_of_words = count_words(file_contents)
    print(f"Amount of words in the book: {number_of_words}")
    chars = count_chars(file_contents)
    print(f"Amount of each character: \n{chars}")

def read_file(path):
    with open(path) as f:
        return f.read()


def count_words(file):
    words = file.split()
    return len(words)


def count_chars(words):
    lower_words = words.lower().split()
    char_dict = {}
    for words in lower_words:
        for char in words:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


main()