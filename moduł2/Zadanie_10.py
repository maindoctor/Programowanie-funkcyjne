def concat_strings(*args):
    return ' '.join(args)

test1 = concat_strings("Hello", "world!")
print("Test 1:", test1)

test2 = concat_strings("This", "is", "a", "test")
print("Test 2:", test2)

test3 = concat_strings("I", "don't", "like", "Python!")
print("Test 3:", test3)
