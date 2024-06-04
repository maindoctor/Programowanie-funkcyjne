def custom_sort(input_list, key_func):
    return sorted(input_list, key=key_func)

def key_func(item):
    return len(item)

input_list = ["abc", "defg", "hi", "jklmn", "o"]
result = custom_sort(input_list, key_func)
print(result)
