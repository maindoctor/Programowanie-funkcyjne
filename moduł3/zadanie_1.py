def double_list_elements(input_list):
    doubled_list = []

    for num in input_list:
        doubled_list.append(num * 2)
    
    return doubled_list

original_list = [1, 2, 3, 4, 5]
doubled_elements = double_list_elements(original_list)
print("Lista pierwotna:", original_list)
print("Lista z podwojonymi elementami:", doubled_elements)
