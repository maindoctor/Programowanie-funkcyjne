def generate_numbers(n):
    for i in range(1, n + 1):
        print(f"Generowanie liczby: {i}")
        yield i

numbers_generator = generate_numbers(5)

for num in numbers_generator:
    print("Otrzymana liczba:", num)