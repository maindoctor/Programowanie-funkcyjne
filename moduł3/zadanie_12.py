def rotate_list(input_list, steps):
    if not input_list:
        return input_list  
    steps %= len(input_list)  
    return input_list[-steps:] + input_list[:-steps]

input_list = [1, 2, 3, 4, 5]
result = rotate_list(input_list, 2)
print(result)
