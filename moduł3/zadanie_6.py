def map_nested(func, nested_list):
    if isinstance(nested_list, list):
        return [map_nested(func, item) for item in nested_list]
    else:
        return func(nested_list)

def double(num):
    return num * 2

nested_list = [1, [2, 3], [4, [5, 6]], 7]

result = map_nested(double, nested_list)
print(result)
