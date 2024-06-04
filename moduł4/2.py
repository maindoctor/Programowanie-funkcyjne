def zmien_litery(tekst):
    nowy_tekst = ""
    for znak in tekst:
        if znak.islower():
            nowy_tekst += znak.upper()
        elif znak.isupper():
            nowy_tekst += znak.lower()
        else:
            nowy_tekst += znak
    return nowy_tekst


tekst = "Hello World!"
wynik = zmien_litery(tekst)
print(wynik) 
