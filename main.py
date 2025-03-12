import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    
    return file_contents

from stats import get_word_count
from stats import num_characters
from stats import sorted_list

def main():
    text = get_book_text(sys.argv[1])
    count = get_word_count(text)
    characters = num_characters(text)
    sorted_chars = sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["character"]
        count = item["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()