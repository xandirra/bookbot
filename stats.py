def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

def num_characters(text):
    num_characters = {}
    characters = text.lower()
    for char in characters:
        if char not in num_characters:
            num_characters[char] = 1
        else:
            num_characters[char] += 1

    return num_characters

def sort_on_count(dictionary):
    return dictionary["count"]

def sorted_list(num_characters):
    list = []
    for char, count in num_characters.items():
        if char.isalpha() == True:
            dict = {"character": char, "count": count}
            list.append(dict)
    list.sort(reverse=True, key=sort_on_count)
    return list


