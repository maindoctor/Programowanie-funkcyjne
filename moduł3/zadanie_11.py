def find_max_min_diff(input_list):
    if not input_list:
        return None  
    max_val = max(input_list)
    min_val = min(input_list)
    return max_val - min_val

input_list = [1, 5, 3, 9, 2, 7]
result = find_max_min_diff(input_list)
print(result)
