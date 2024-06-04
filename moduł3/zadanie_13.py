def split_list(input_list, length):
    return [input_list[i:i+length] for i in range(0, len(input_list), length)]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = split_list(input_list, 3)
print(result)
