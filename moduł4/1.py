def suma_parzystych(liczby):
    suma = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            suma += liczba
    return suma

lista_liczb = [1, 2, 3, 4, 5, 6]
wynik = suma_parzystych(lista_liczb)
print(wynik)  
