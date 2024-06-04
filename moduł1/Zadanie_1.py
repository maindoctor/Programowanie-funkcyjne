def apply_twice(func, value):
    return func(func(value))

def square(x):
    return x * x

result = apply_twice(square, 3)
print("Wynik:", result)
