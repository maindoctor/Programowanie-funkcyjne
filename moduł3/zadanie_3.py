def recursive_sum(nested_list):
    total_sum = 0
    
    for element in nested_list:
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element
    
    return total_sum

nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
total = recursive_sum(nested_list)
print("Suma wszystkich liczb w zagnieżdżonych listach:", total)
