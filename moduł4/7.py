def polacz_slowniki(*slowniki):
    wynik = {}
    for slownik in slowniki:
        for klucz, wartosc in slownik.items():
            if klucz in wynik:
                wynik[klucz] += wartosc
            else:
                wynik[klucz] = wartosc
    return wynik

slownik1 = {'a': 1, 'b': 2, 'c': 3}
slownik2 = {'a': 2, 'c': 4, 'd': 1}
slownik3 = {'a': 1, 'b': 1, 'e': 5}

wynik = polacz_slowniki(slownik1, slownik2, slownik3)
print(wynik)
