import sys
from stats import get_num_words, count_characters

def get_book_text(path):
    #print(f"Reading book from {path}")    
    with open(path) as f:
        file_content = f.read()
    return file_content

def sort_on(item):
    """
    Returns the second element of a tuple.
    """
    return item["count"]

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    book_dict = count_characters(book_text)
    #print(book_dict)
    book_dict.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----")
    #print(book_dict)
    for entry in book_dict:
        print(f"{entry['letter']}: {entry['count']}")
    print("============= END ===============")
    
main()
