palavra = input('Digite uma palavra: ')
for letra in range(len(palavra),0,-1):
    print(palavra[:letra])
