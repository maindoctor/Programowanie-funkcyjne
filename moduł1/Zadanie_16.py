def compose(f, g):
    def composed_function(*args, **kwargs):
        return f(g(*args, **kwargs))
    
    return composed_function

def add_one(x):
    return x + 1

def square(x):
    return x * x

composed_function = compose(add_one, square)

result = composed_function(3)
print("Wynik kompozycji funkcji:", result)
