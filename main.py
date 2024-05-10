def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    print(f"Book word count: {word_count}")


def get_num_words(words: str) -> int:
    words = words.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents


main()
