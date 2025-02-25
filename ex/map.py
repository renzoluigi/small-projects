def converter_fahrenheit(celsius):
    return 1.8 * celsius + 32

c = [22.5, 40, 13, 29, 34]
fahrenheits = list(map(converter_fahrenheit,c))
print(fahrenheits)

valores = [21, 5, 34, 8, 16, 7, 3]
soma_pares = sum(map(lambda x:x if x % 2 == 0 else 0, valores))
soma_impares = sum(map(lambda x:x if x % 2 != 0 else 0, valores))
print(soma_pares, soma_impares)