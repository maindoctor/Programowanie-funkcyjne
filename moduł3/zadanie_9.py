def zip_with_index(input_list):
    return [(index, value) for index, value in enumerate(input_list)]

input_list = ['a', 'b', 'c', 'd', 'e']

result = zip_with_index(input_list)

print(result)
