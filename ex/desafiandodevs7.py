def passou_ou_nao(dados):
    resultado = {}
    for nome,notas in dados.items():
        if sum(notas) / 4 >= 5:
            resultado[nome] = 'passou'
        elif 4 < sum(notas) / 4 < 5:
            resultado[nome] = 'recup. final'
        else:
            resultado[nome] = 'reprovado'
    return resultado
print(passou_ou_nao({'renan':[6,5,4,3],'sofia':[9,6,8,9],'lucas':[4,7,9,2]}))