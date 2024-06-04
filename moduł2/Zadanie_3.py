def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_sequence = fibonacci()
print("Pierwsze 10 liczb ciągu Fibonacciego:")
for _ in range(10):
    print(next(fib_sequence))
