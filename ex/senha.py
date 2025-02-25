def verificar_senha(senha,senha_entrada):
    if senha_entrada == senha:
        return True
    else:
        return False

password = 'da1irwdDG!1CXey'
erros = 0
pswrd = ''
while verificar_senha(password,pswrd) is False and erros < 3:
    pswrd = input('Digite a sua senha: ')
    if verificar_senha(password,pswrd):
        print('\033[34mBem-Vindo!\033[m')
    else:
        erros += 1
        print(f'\033[31mSenha incorreta, você tem mais {3 - erros} chances\033[m')
