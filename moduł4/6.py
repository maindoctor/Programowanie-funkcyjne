def zastosuj_funkcje_do_listy(lista, funkcja):
    return [funkcja(element) for element in lista]

lista = [1, 2, 3, 4, 5]

def podwoj(x):
    return x * 2

wynik = zastosuj_funkcje_do_listy(lista, podwoj)
print(wynik)  
