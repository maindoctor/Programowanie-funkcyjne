from itertools import product

list1 = ['A', 'B']
list2 = ['C', 'D']

combinations = list(product(list1, list2))

print("Wszystkie możliwe kombinacje liter z listy 1 i listy 2:")
for combination in combinations:
    print(combination)