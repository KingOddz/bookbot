def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    dict = count_chars(text)
    converted_list = cnvrt_dict(dict)
    converted_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for x in converted_list:
        character = x["char"]
        count = x["num"]
        print(f"the {character} character was found {count} times")
    print("--- End report ---")

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

def sort_on(dict):
    return dict["num"]

def cnvrt_dict(dict):
    counts = []
    for x in dict:
        counts.append({"char" : x, "num" : dict[x]})
    return counts


main()