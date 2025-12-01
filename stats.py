
from main import get_book_text

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char == ' ' or char == '\n':
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def convert_to_sorted_list(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list

def main(filepath):
    book_text = get_book_text(filepath)

    # Word count
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words.\n")

    # Character count
    char_counts = count_characters(book_text)
    sorted_char_list = convert_to_sorted_list(char_counts)

    # Print report
    print("Character frequency report:")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")


