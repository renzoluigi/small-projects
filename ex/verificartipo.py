def verificar_tipo(numero):
    if isinstance(numero,float):
        return 'Número é decimal'
    elif isinstance(numero,int):
        return 'Número é inteiro'
    else:
        return 'Não é um dado numérico'


valor = input('Digite algo: ')
if type(valor) is float:
    print('É decimal')
else:
    print('É inteiro')
#errado