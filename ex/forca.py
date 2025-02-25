from tkinter import *
from random import choice
animation = ""
lst = []
errors = 0
jogo_ativo = False
repeated_animations = []
pontuacao = 0
def forca():
    global errors,animation,lst, jogo_ativo, repeated_animations,pontuacao
    lst = []
    repeated_animations.append(animation)
    famous_animations = ["O Rei Leao", "Toy Story", "Shrek", "Frozen", "Procurando Nemo", "A Bela e a Fera",
                         "Os Incriveis", "Up", "Wall E", "Monstros SA", "Ratatouille", "Kung Fu Panda",
                         "A Era do Gelo", "Moana", "Zootopia", "O Fantastico Sr Raposo", "Coraline",
                         "A Noiva Cadaver", "Meu Malvado Favorito", "Como Treinar o Seu Dragao", "Madagascar",
                         "Enrolados", "Viva A Vida e uma Festa", "Encanto", "Lilo e Stitch", "Ponyo",
                         "Kubo e as Cordas Magicas", "Akira", "Princesa Mononoke", "A Viagem de Chihiro"]
    while animation in repeated_animations:
        animation = choice(famous_animations).lower()
    jogo_ativo = True
    errors = 0
    for letter in animation:
        if letter.isalpha():
            lst.append('_')
        else:
            lst.append(' ')
    palavra['text'] = ' '.join(lst)
    qtd_errors['text'] = f'{errors} erros'
    qtd_errors['fg'] = 'black'
    texto_do_jogo['text'] = ''
    alerta['text'] = ''
    pts['text'] = f'Pontuação: {pontuacao}'
    pts['fg'] = 'black'
def verificar_letra():
    global errors, animation, lst, jogo_ativo, pontuacao
    if not jogo_ativo:
        return
    if errors == 1:
        qtd_errors['text'] = f'{errors} erro'
        qtd_errors['fg'] = 'red'
    if errors > 1:
        qtd_errors['text'] = f'{errors} erros'
        qtd_errors['fg'] = 'red'
    letter = entrada.get().lower().strip()
    entrada.delete(0, END)
    if len(letter) != 1 or not letter.isalpha():
        alerta['text'] = "Insira apenas uma letra válida."
        alerta['fg'] = 'red'
        return
    if letter in lst:
        alerta['text'] = "Você já acertou essa letra!"
        alerta['fg'] = 'orange'
        return
    if letter in animation:
        for i, char in enumerate(animation):
            if char == letter:
                lst[i] = letter
        alerta['text'] = "Boa! Você acertou uma letra."
        alerta['fg'] = 'green'
    else:
        errors += 1
        alerta['text'] = "Letra errada!"
        alerta['fg'] = 'red'
    palavra['text'] = ' '.join(lst)
    if errors == 1:
        qtd_errors['text'] = f'{errors} erro'
        qtd_errors['fg'] = 'red'
    else:
        qtd_errors['text'] = f'{errors} erros'
        qtd_errors['fg'] = 'black'
    qtd_errors['fg'] = 'red' if errors > 0 else 'black'
    if errors == 6:
        texto_do_jogo['text'] = 'FIM DE JOGO! O filme era: ' + animation.title()
        texto_do_jogo['fg'] = 'red'
        pontuacao = 0
        pts['fg'] = 'red'
        jogo_ativo = False
    elif animation == ''.join(lst):
        texto_do_jogo['text'] = 'Parabéns, você acertou o filme!'
        texto_do_jogo['fg'] = 'green'
        pontuacao += 1
        jogo_ativo = False

janela = Tk()

janela.title('Jogo da Forca')
janela.geometry('600x400')

texto = Label(janela,text='Bem vindo ao jogo da forca, você tem 6 chances de acerto, ao clicar em "Sortear novo filme" você começa um novo jogo!',font=("Arial", 8))
texto.grid()

botao = Button(janela,text='Sortear novo filme',command=forca)
botao.grid(pady=10)

entrada = Entry(janela, width=10)
entrada.grid(padx=10)

enviar = Button(janela,text='Enviar',command=verificar_letra)
enviar.grid(pady=10)

texto_do_jogo = Label(janela,text='')
texto_do_jogo.grid(pady=10)

palavra = Label(janela,text='',font=("Arial", 10))
palavra.grid(pady=10)

alerta = Label(janela,text='')
alerta.grid(pady=10)

qtd_errors = Label(janela,text='')
qtd_errors.grid(pady=10)

pts = Label(janela,text=f'',font=('Arial',14))
pts.place(relx=1, rely=1, anchor="se")

janela.mainloop()
