def max_min(lista):
    return max(lista),min(lista)
lista = []
for cont in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)
print(max_min(lista))