def potegowanie(exponent):
    def podnieś_do_potęgi(liczba):
        return liczba ** exponent
    return podnieś_do_potęgi


kwadrat = potegowanie(2)
sześcian = potegowanie(3)

print(kwadrat(4))  
print(sześcian(2))  
