def conjuntos_uniao(conjunto1,conjunto2):
    uniao = []
    for n in conjunto1:
        uniao.append(n)
    for n in conjunto2:
        for numero in uniao:
            if n != numero:
                uniao.append(n)
    uniao.sort()
    return uniao

cj1 = [1, 3, 6, 9, 12, 15, 18]
cj2 = [1, 2, 4, 6, 8, 10, 12, 16]
print(conjuntos_uniao(cj1,cj2))