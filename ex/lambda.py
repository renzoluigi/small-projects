def dobrar(lista):
    new_list = []
    for numero in lista:
        new_list.append(numero*2)
    return new_list
lista = [1,6,4,13,22]
lista_duplicada = list(map(lambda x:x*2,lista))
print(lista_duplicada)
#ou
print(dobrar(lista))