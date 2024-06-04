def parzyste():
    liczba = 0
    while True:
        yield liczba
        liczba = liczba + 2

generator_parzystych = parzyste()
for _ in range(10):
    print(next(generator_parzystych))