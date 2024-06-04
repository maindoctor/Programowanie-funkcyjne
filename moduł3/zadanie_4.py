def remove_duplicates(input_list):
    output_list = []
    seen = set()
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
    return output_list

input_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 7, 9]
print("Lista pierwotna:", input_list)
unique_list = remove_duplicates(input_list)
print("Lista bez zduplikowanych elementów:", unique_list)
