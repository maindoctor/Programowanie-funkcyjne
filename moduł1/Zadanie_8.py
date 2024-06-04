from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Suma wszystkich liczb w liście:", sum_of_numbers)
