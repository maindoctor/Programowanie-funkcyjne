def analyze_data(data):
    if isinstance(data, list):
        if data == []:
            print("Dane są pustą listą.")
        else:
            first, *rest = data
            print(f"Pierwszy element listy to {first}, a reszta to {rest}.")
    elif isinstance(data, tuple):
        if data == ():
            print("Dane są pustą krotką.")
        else:
            first, *rest = data
            print(f"Pierwszy element krotki to {first}, a reszta to {rest}.")
    elif isinstance(data, set):
        if data == set():
            print("Dane są pustym zbiorem.")
        else:
            first, *rest = data
            print(f"Pierwszy element zbioru to {first}, a reszta to {rest}.")
    else:
        print("Nieznana struktura danych.")

analyze_data([])
analyze_data([7, 2, 3, 4, 5])
analyze_data((7, 2, 3, 4, 5))
analyze_data({7, 2, 3, 4, 5})
