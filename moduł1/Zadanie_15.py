from functools import partial

def add(x, y):
    return x + y

curried_add = partial(add, 5)

wynik = curried_add(3)
print(f"Wynik dodawania: {wynik}")
