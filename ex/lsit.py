#Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"
notas = list()
for c in range(1,5):
    n = float(input(f'Digite a {c}° nota: '))
    notas.append(n)
notas = sum(notas)
media = notas / 4
if media >= 7:
    print(f'Média final: {media}\n Situação: \033[32MAPROVADO\033[m')
elif 5 <= media < 6.9:
    print(f'Média final: {media}\n Situação: \033[34mRECUPERAÇÃO!\033[m')
else:
    print(f'Média final: {media}\n Situação: \033[31REPROVADO!\033[m')