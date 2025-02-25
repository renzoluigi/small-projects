from random import choice


def escolher_palavra(arquivo):
    with open(arquivo, 'r') as arquivo:
        lista = arquivo.read().splitlines()
        arquivo.close()
        return choice(lista)
def forca_game(palavra):
    forca = '_'*len(palavra)
    erros = 1
    print('-' * 40)
    print(f'{'BEM-VINDO AO JOGO DA FORCA!':^40}')
    print('-' * 40)
    while True:
        letra = input('Digite um letra: ').lower()[0]
        if letra in palavra:
            nova_forca = ""
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    nova_forca += letra
                else:
                    nova_forca += forca[i]
            forca = nova_forca
            print(f'A palavra é: \033[34m{forca}\033[m')
            if forca == palavra:
                print('\033[32mParabéns, você venceu!\033[m')
                break
        else:
            if erros == 6:
                print(f'\033[31m-> Você errou pela {erros}ª vez. FIM!\033[m')
                break
            else:
                print(f'\033[31m-> Você errou pela {erros}ª vez. Tente de novo!\033[m')
                erros += 1


forca_game(escolher_palavra('palavrasforca.txt'))
