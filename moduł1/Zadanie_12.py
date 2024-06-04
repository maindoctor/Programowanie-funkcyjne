import functools

def razy(x):
    return x * 3

razy_part = functools.partial(razy)

liczba = 5
wynik = razy_part(liczba)
print(f"{liczba} razy 3 = {wynik}")