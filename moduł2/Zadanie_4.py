numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

squared_numbers = [square for number in numbers if (square := number ** 2) > 10]

print("Kwadraty liczb większych niż 10:", squared_numbers)
