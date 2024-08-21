def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))
    print(count_chars(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    dict = {}
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lower_text = text.lower()
    for x in characters:
        dict[x] = lower_text.count(x)
    return dict

main()