words = ["jabłko", "banan", "gruszka", "śliwka", "arbuz", "malina", "truskawka", "ananas", "mango"]

long_words = list(filter(lambda word: len(word) > 5, words))

print("Słowa z listy o długości większej niż 5 liter:", long_words)