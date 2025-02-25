nomes = []
arquivo_entrada = input('Digite o nome do arquivo de entrada: ')
try:
    with open(arquivo_entrada, 'r') as arquivo:
        for linha in arquivo:
            nome = linha.strip().split()
            nomes.append(nome)
    arquivo.close()
except FileNotFoundError:
    print(f'Arquivo de entrada não encontrado.')
nomes = sorted(nomes)
arquivo_saida = input('Digite o nome do arquivo de saida: ')
try:
    with open(arquivo_saida, 'w+') as arq:
        for nome in nomes:
            arq.write(f'{nome}\n')
except FileNotFoundError:
    print(f'Arquivo de saída não encontrado.')
else:
    arq.close()
