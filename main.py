def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_book_character_count(text.lower())
    filtered_char_count = filter_alpha_chars(char_count)
    
    # Print the Report:
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char, count in filtered_char_count:
        print(f"The '{char}' characther was found {count}")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def get_book_character_count(text):
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def filter_alpha_chars(char_count):
    filtered = [(char, count) for char, count in char_count.items() if char.isalpha()]
    return sorted(filtered, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    main()
