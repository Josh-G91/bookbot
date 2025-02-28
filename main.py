from stats import get_num_words
from stats import create_word_count_dict
from stats import sort_character_dict

def get_book_text(path:str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    frankenstein_contents = get_book_text("books/frankenstein.txt")
    total_words = get_num_words(frankenstein_contents)
    total_characters = create_word_count_dict(frankenstein_contents)
    sorted_characters = sort_character_dict(total_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f'Found {total_words} total words')
    print("--------- Character Count -------")
    for char_dicts in sorted_characters:
        item = list(char_dicts.items())[0]
        if not item[0].isalpha():
            continue
        print(f'{item[0]}: {item[1]}')
    print("============= END ===============")
if __name__ == "__main__":
    main()

