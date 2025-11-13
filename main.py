import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary
from stats import print_sorted_dictionary


def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    #book_path = 'books/frankenstein.txt'  # Path to your book file
    #book_path = sys.argv[1] if len(sys.argv) > 1 else book_path
    book_path = sys.argv[1] #if len(sys.argv) > 1 else 'books/frankenstein.txt'
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    character_count = get_num_characters(book_text)
    sorted_count = sort_dictionary(character_count)
    print("--------- Character Count -------")
    print_sorted_dictionary(sorted_count)
    print("============= END ===============")

if __name__ == "__main__":
    main()