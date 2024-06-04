def count_unique_elements(input_list):
    unique_elements = set(input_list)
    return len(unique_elements)

input_list = [1, 2, 3, 1, 2, 4, 5, 3, 6]
result = count_unique_elements(input_list)
print(result)
