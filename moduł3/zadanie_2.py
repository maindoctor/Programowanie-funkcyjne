def filter_long_words(string_list):
    avg_length = sum(len(word) for word in string_list) / len(string_list)
    
    filtered_list = [word for word in string_list if len(word) > avg_length]
    
    return filtered_list

words = ["apple", "banana", "orange", "kiwi", "pineapple"]
filtered_words = filter_long_words(words)
print("Lista pierwotna:", words)
print("Lista zawierająca tylko stringi dłuższe niż średnia długość:", filtered_words)
