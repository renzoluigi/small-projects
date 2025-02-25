def soma_de_inteiros(n1, n2):
    if isinstance(n1,float) or isinstance(n2,float):
        raise ValueError('Um dos valores digitados não é inteiro.')
    if n1 < 0 or n2 < 0:
        raise ValueError('n1 e n2 não podem ser negativos.')
    return n1+n2

print(soma_de_inteiros(1,-4))