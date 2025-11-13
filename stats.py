def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_characters = {}
    if len(text) == 0:
        return num_characters
    for char in text:
        letters = char.lower()
        if letters not in num_characters:
            num_characters[letters] = 0
        num_characters[letters] +=1
    return num_characters

def sort_dictionary(dict1):
    sorted_list = []
    for k, v in dict1.items():
        if k.isalpha() == True:
            sorted_list.append({"char": k, "num": v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_sorted_dictionary(sorted_list):
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

def sort_on(items):
    return items["num"]