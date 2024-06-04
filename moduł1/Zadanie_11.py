def sortuj(lista):
    lista.sort(key=lambda x: len(x))
    return lista

lista1 = ["audi", "bmw", "volkswagen", "honda", "opel"]
lista2 = sortuj(lista1)
print(lista2)
