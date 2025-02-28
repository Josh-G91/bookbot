def get_num_words(book: str) -> int:
    return len(book.split()) 

def create_word_count_dict(book: str) -> int:
    lower_case_book = list(book.lower())
    characters = set(lower_case_book)
    return {char:lower_case_book.count(char) for char in characters}


def sort_character_dict(characters: dict) -> list[dict]:
    char_dicts = [{char:count} for char, count in zip(characters.keys(), characters.values())]
    char_dicts.sort(reverse=True, key=lambda d: list(d.values())[0])
    return char_dicts
    

    


