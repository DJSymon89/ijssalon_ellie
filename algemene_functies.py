def mijn_functie_1(x):
    return x ** 2

test_values = [2, 4, 10, 12]
results = {x: mijn_functie_1(x) for x in test_values}

print(results)

def mijn_functie_2(a, b):
    return [a + b, a - b, a * b, a // b]

test_values = [(12, 3), (12, 2), (10, 5), (100, 20)]
results = {args: mijn_functie_2(*args) for args in test_values}

print(results)