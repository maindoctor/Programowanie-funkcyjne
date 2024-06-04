def podziel_liste(lista, max_dlugosc):
    
    if max_dlugosc <= 0:
        raise ValueError("Maksymalna długość musi być większa od 0")
    
    return [lista[i:i + max_dlugosc] for i in range(0, len(lista), max_dlugosc)]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_dlugosc = 3
wynik = podziel_liste(lista, max_dlugosc)
print(wynik)  
