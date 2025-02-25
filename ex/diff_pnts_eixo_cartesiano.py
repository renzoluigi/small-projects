from math import sqrt
x1 = int(input('Qual a medida do ponto x1? '))
x2 = int(input('Qual a medida do ponto x2? '))
y1 = int(input('Qual a medida do ponto y1? '))
y2 = int(input('Qual a medida do ponto y2? '))
distância = sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'A distância entre A e é de: {distância:.2f}.')