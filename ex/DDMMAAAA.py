data = input('Digite o seu ano de nascimento no formato "DDMMAAAAA": ')
dia = int(data[0:2])
mes = int(data[2:4])
ano = int(data[4:8])
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']
if 1 <= mes <= 12:
    mes = meses[mes-1]
else:
    print('ERRO! Você digitou algo errado!')
print(f'{dia} de {mes} de {ano}.')