def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Wystąpił błąd podczas wywołania funkcji: {e}")
            return None
    return wrapper

@safe_function
def divide(a, b):
    return a / b

result1 = divide(10, 2)
print("Wynik dzielenia:", result1)

result2 = divide(10, 0)
print("Wynik dzielenia:", result2)
