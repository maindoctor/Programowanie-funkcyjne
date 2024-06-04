def zastosuj_funkcje_do_krotek(lista_krotek, funkcja):
    return [funkcja(*krotka) for krotka in lista_krotek]

lista_krotek = [(1, 2), (3, 4), (5, 6)]

def dodaj(x, y):
    return x + y

wynik = zastosuj_funkcje_do_krotek(lista_krotek, dodaj)
print(wynik) 
