from random import randint

def marcalinha(msg):
    print('-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)

cores = {
    'vermelho': '\033[31m',
    'azul': '\033[34m',
    'verde': '\033[32m',
    'resetar': '\033[m'
}

pergunta = 'S'
marcalinha('BEM VINDO AO JOGO DA ADIVINHAÇÃO')
pontos = 0
nome = input('Digite seu nome: ').strip()
while True:
    erros = 0
    chance = 6
    aleatorio = randint(0, 10)
    print(aleatorio)
    if pergunta == 'S':
            while chance > 0:
                erros += 1
                chance -= 1
                try:
                    numero = int(input('Adivinhe o número que eu escolhi: '))
                except (TypeError, ValueError):
                    print('ERRO! Insira um numero inteiro.')
                except KeyboardInterrupt:
                    print('ERRO! Nenhum caractere foi digitado.')
                else:
                    if numero == aleatorio:
                        match erros:
                            case 1:
                                print(f'{cores['azul']}Parabéns você acertou na {erros}ª tentativa, + 100 pontos.{cores['resetar']}')
                                pontos += 100
                                break
                            case 2:
                                print(f'{cores['azul']}Parabéns você acertou na {erros}ª tentativa, + 70 pontos.{cores['resetar']}')
                                pontos += 70
                                break
                            case 3:
                                print(f'{cores['azul']}Parabéns você acertou na {erros}ª tentativa, + 50 pontos.{cores['resetar']} ')
                                pontos += 50
                                break
                            case 4:
                                print(f'{cores['azul']}Parabéns você acertou na {erros}ª tentativa, + 30 pontos.{cores['resetar']}')
                                pontos += 30
                                break
                            case 5:
                                print(f'{cores['azul']}Parabéns você acertou na {erros}ª tentativa, + 20 pontos.{cores['resetar']} ')
                                pontos += 20
                                break
                            case 6:
                                print(f'{cores['azul']}Parabéns você acertou na {erros}ª tentativa, + 10 pontos.{cores['resetar']}' )
                                pontos += 10
                                chance += 1
                                break
                    else:
                        if chance == 1:
                            print(f'{cores['vermelho']}Você errou pela {erros}ª vez, você tem mais {chance} chance.{cores['resetar']}')
                        elif chance == 0:
                            print(f'{cores['vermelho']}Você errou pela {erros}ª vez, FIM DE JOGO!{cores['resetar']}')
                        else:
                            print(f'{cores['vermelho']}Você errou pela {erros}ª vez, você tem mais {chance} chances.{cores['resetar']}')

    if chance == 0:
        break
    pergunta = input('Deseja continuar? [S/N] ').upper()[0]
    if pergunta == 'N':
        print(f'{cores['azul']}Pontuação de {pontos} pontos registrada!{cores['resetar']}')
        marcalinha('ATÉ MAIS!')
        pessoas = list()
        pontuacao = list()
        arquivo = open('recordes.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            if not linha or ':' not in linha:
                continue
            n, pts = linha.split(':')
            pessoas.append(n)
            pontuacao.append(pts)
        listageral = zip(pessoas, pontuacao)
        listageral = sorted(listageral, key=lambda x: x[1], reverse=True)
        with open('recordes.txt', 'w') as arquivo:
            for name, points in listageral:
                arquivo.write(f"{name}: {points}\n")
            arquivo.write(f"{nome}: {pontos}\n")
        p = input('Deseja ver a lista de recordes? [S/N] ').lower()
        if p == 's':
            for c in range(len(listageral)):
                print(f'{c + 1}ª{listageral[c][0]:^10}: {listageral[c][1]} pontos')
        arquivo.close()
        break
    else:
        while pergunta not in 'SN':
            print(f'{cores['vermelho']}Opção inválida, tente novamente.{cores['resetar']}')
            pergunta = input('Deseja continuar? [S/N] ').upper()[0]
