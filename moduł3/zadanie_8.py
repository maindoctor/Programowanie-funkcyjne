def partition_list(input_list, condition):
    true_list = [item for item in input_list if condition(item)]
    false_list = [item for item in input_list if not condition(item)]
    return true_list, false_list

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

condition = lambda x: x % 2 == 0

true_list, false_list = partition_list(input_list, condition)

print("Elementy spełniające warunek:", true_list)
print("Pozostałe elementy:", false_list)
