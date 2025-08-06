import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import total_words
from stats import characters
from stats import sort_on
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    text = get_book_text(sys.argv[1])
    num_words = total_words(text)
    chars = characters(text)
    chars_list = []
    for letter,num in chars.items():
        if letter.isalpha():
            chars_list.append({"char": letter,"num": num})
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars_list.sort(reverse = True, key = sort_on)
    for c in chars_list:
        print(f"{c['char']}: {c['num']}")

main()