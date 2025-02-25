def conv(num):
    convertido = num / 1048576
    return convertido


arquivo = open('usuarios.txt', 'r')
lista = list()
dados = dict()
total = 0
for linha in arquivo:
    info = linha.split()
    s = conv(int(info[1]))
    total += s
    dados = {'nome': info[0], 'mb':s}
    lista.append(dados)
arquivo.close()
#print(f'{cont + 1} {info[0].replace('\n', ''):20} {byte} MB')
print('ACME Inc.     Uso do espaço em disco pelos usuários')
print('-'*52)
print(f'Nr. {'Usuário':15} {'Espaço utilizado':10} {'% do uso':>14}')
for c in range(0,len(lista)):
    porcent = lista[c]['mb'] / total * 100
    print(f'{c + 1:<3} {lista[c]['nome']:15} {lista[c]['mb']:10.2f} MB {porcent:15.2f}%')
print()
print(f'Espaço total ocupado: {total:.2f}')
print(f'Espaço médio ocupado: {total/len(lista):.2f}')
