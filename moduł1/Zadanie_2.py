def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_5 = make_multiplier(5)
multiply_by_10 = make_multiplier(10)

print("Wynik mnożenia 3 przez 5:", multiply_by_5(3))
print("Wynik mnożenia 3 przez 10:", multiply_by_10(3))
