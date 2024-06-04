import itertools

def generuj_permutacje(lista):
    return list(itertools.permutations(lista))

lista = [1, 2, 3]
wynik = generuj_permutacje(lista)
print(wynik)  
