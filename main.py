import sys

from stats import create_word_count_dict, get_num_words, sort_character_dict


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def run_sys_command() -> str:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]


def main():
    path_to_book = run_sys_command()
    book_contents = get_book_text(path_to_book)
    total_words = get_num_words(book_contents)
    total_characters = create_word_count_dict(book_contents)
    sorted_characters = sort_character_dict(total_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book: {path_to_book.split("/")[1].strip("txt")}")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_dicts in sorted_characters:
        item = list(char_dicts.items())[0]
        if not item[0].isalpha():
            continue
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
