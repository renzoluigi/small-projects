print('-'*50)
print('BEM VINDO AO POSTO SHELL')
print('-'*50)
litros = int(input('Quantos litros você deseja? '))
tot = litros
tipo = input('Tipo de combustível: (A - Álcool, G - Gasolina) ')
if tipo[0] in 'Aa':
    tot *= 1.90
    if litros < 20:
        tot -= 3/100*tot
    else:
        tot -= 5/100*tot
elif tipo[0] in 'Gg':
    tot *= 2.50
    if litros < 20:
        tot -= 4/100*tot
    else:
        tot -= 6/100*tot
else:
    print('Você não digitou uma opção válida.')
print(f'O valor total é R${tot:.2f}')
