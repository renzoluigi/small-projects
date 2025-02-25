def ultimo_elemento(lista):
    if isinstance(lista,list) and lista:
        return lista[-1]
    else:
        return None

numeros = [9,4,7,3]
print(ultimo_elemento(numeros))