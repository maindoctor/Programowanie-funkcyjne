from functools import partial

def add(x, y):
    return x + y

add_5 = partial(add, 5)

result = add_5(3)
print("Wynik dodawania 5 do 3:", result)
