def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_generator = generate_fibonacci()

# Wyświetlenie pierwszych 10 liczb Fibonacciego
for _ in range(10):
    print(next(fibonacci_generator))
