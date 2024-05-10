#!/usr/bin/env python3
import argparse


def main(file_path):
    book_content = get_book_text(file_path)
    word_count = get_num_words(book_content)
    letter_count = get_letter_count(book_content)

    def print_report():
        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count} words found in the document\n")
        letter_string_template = "The '{}' character was found {} times."
        for letter in letter_count:
            letter_str = letter_string_template.format(letter, letter_count[letter])
            print(letter_str)
        print("--- End report ---")

    print_report()


def get_num_words(words: str) -> int:
    words = words.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents


def get_letter_count(text: str) -> dict:
    letters_count = {}
    text = text.lower()
    letters = sorted([letter for letter in text if letter.isalpha()])
    for letter in letters:
        if letter not in letters_count:
            letters_count[letter] = 1
        else:
            letters_count[letter] += 1
    return letters_count


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path to text file")
args = parser.parse_args()


main(args.path)
