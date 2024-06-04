def flatten_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened_list.extend(flatten_list(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list

nested_list = [1, [2, 3], [4, [5, 6]], 7]

result = flatten_list(nested_list)
print(result)
