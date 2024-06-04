def calculate_tuple_stats(data):
    if not isinstance(data, tuple):
        raise TypeError("Oczekiwano krotki liczb")

    suma = 0
    iloczyn = 1

    for element in data:
        suma += element
        iloczyn *= element

    return suma, iloczyn

moja_krotka = (1, 2, 3, 4, 5)

wynik_sumy, wynik_iloczynu = calculate_tuple_stats(moja_krotka)
print("Suma elementów krotki:", wynik_sumy)
print("Iloczyn elementów krotki:", wynik_iloczynu)
