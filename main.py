from typing import List, Dict


def print_report(path, words, letters_dict) -> None:
    print(f"____Begin report of {path}")
    print(f"{words} words found in the document")

    letters_dict = dict(sorted(letters_dict.items(), key=lambda x: x[1], reverse=True))
    for key in letters_dict:
        print(f"{key} character occurs {letters_dict[key]} times")


def get_letters_count(text: str) -> Dict[str, int]:
    char_dict = {}
    for letter in text:
        if letter.isalpha():
            lower_letter = letter.lower()
            if lower_letter in char_dict:
                char_dict[lower_letter] += 1
            else:
                char_dict[lower_letter] = 1

    return char_dict


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main() -> None:
    path: str = "books/frankenstein.txt"
    text: str = get_book_text(path)
    num_words: int = get_word_count(text)
    letters_dict: Dict[str, int] = get_letters_count(text)
    print_report(path, num_words, letters_dict)


if __name__ == "__main__":
    main()
