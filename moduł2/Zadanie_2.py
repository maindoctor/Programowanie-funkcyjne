from itertools import combinations

def generate_combinations(elements):
    all_combinations = list(combinations(elements, 2))
    return all_combinations

elements = [1, 2, 3, 4]
result = generate_combinations(elements)
print("Wszystkie możliwe 2-elementowe kombinacje:", result)
