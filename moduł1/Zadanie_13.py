def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

liczba = 5
wynik = calculate_factorial(liczba)
print(f"Silnia liczby {liczba} = {wynik}")