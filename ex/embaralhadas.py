from random import shuffle, choice


def selecionar_palavra(arquivo):
    with open(arquivo,'r') as arq:
        lista = arq.read().splitlines()
        arq.close()
        return choice(lista)


def embaralhar_palavra(p):
    lista_letras = list(p)
    shuffle(lista_letras)
    embaralhada = ''.join(lista_letras)
    return embaralhada


def jogo(palavra_embaralhada):
    erros = 1
    print(f'A palavra embaralhada é: \033[96m{palavra_embaralhada}\033[m')
    while True:
        desembaralhar = input('Digite a palavra desembaralhada: ').lower()
        if desembaralhar == palavra:
            print('\033[34mParabéns você acertou!!\033[m')
            break
        else:
            if erros == 6:
                print(f'\033[31m-> Você errou pela {erros}ª vez. FIM!\033[m')
                break
            else:
                print(f'\033[31m-> Você errou pela {erros}ª vez. Tente de novo!\033[m')
                erros += 1


palavra = selecionar_palavra('palavrasforca.txt')
palavra_emb= embaralhar_palavra(palavra)
jogo(palavra_emb)
