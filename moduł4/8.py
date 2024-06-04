def najczestszy_element(lista):
    if not lista:
        return None
    
    licznik = {}
    for element in lista:
        if element in licznik:
            licznik[element] += 1
        else:
            licznik[element] = 1

    
    najczestszy = max(licznik, key=licznik.get)
    
    return najczestszy


lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
wynik = najczestszy_element(lista)
print(wynik)  
