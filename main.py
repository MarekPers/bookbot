def main():
    # File contents
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    print(f"--- Begin report of {file_path} ---")

    number_of_words = count_words(file_contents)
    print(f"Amount of words in the book: {number_of_words}")

    # Declaring dictionary w/ character amounts
    chars = count_chars(file_contents)
    # Converting dict to list of dicts [{x:1},{y:2},..., etc.]
    chars_list = list_conversion(chars)
    #Sorting & spilling results
    sorted_spill(chars_list)


def sorted_spill(char_list):
    sorted_list = sorted(char_list, key=lambda x: x["value"], reverse=True)
    for dict in sorted_list:
        if dict["key"].isalpha():
            print(f"The '{dict["key"]}' character was found {dict["value"]} times.")
    print("--- End report ---")


def list_conversion(char_dict):
    return [{"key": k, "value": v} for k, v in char_dict.items()]


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


### DO NOT TOUCH BELOW ###
def read_file(path):
    with open(path) as f:
        return f.read()


def count_words(file):
    words = file.split()
    return len(words)


main()