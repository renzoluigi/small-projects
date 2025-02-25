telefone = input('Numero de telefone: ')
digitos = len(telefone)
if digitos == 7:
    print(f'\033[31mO telefone tem {digitos} dígitos, o numero três foi colocado para completar.\033[m')
    telefone += '3'
    print(f'Telefone corrigido sem formatação: \033[34m{telefone}\033[m')
    print(f'Telefone corrigido formatado: \033[34m{telefone[0:4]}-{telefone[4:]}\033[m')
elif digitos < 7:
    print(f'\033[31mERRO! O numero digitado tem apenas {digitos} dígito(s).\033[m')
elif digitos > 8:
    print(f'\033[31mERRO! O numero digitado tem dígitos demais.\033[m')
