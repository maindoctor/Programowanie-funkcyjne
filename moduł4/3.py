def filtruj_parzyste_wartosci(slownik):
    nowy_slownik = {}
    for klucz, wartosc in slownik.items():
        if isinstance(wartosc, int) and wartosc % 2 == 0:
            nowy_slownik[klucz] = wartosc
    return nowy_slownik


przykladowy_slownik = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 'nie liczba',
    'f': 6
}
wynik = filtruj_parzyste_wartosci(przykladowy_slownik)
print(wynik) 