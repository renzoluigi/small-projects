from random import choice
from tkinter import *
def computer_choose():
    return choice(['Pedra','Papel','Tesoura'])

game = Tk()
game.title('JoKenPo')
window_width = 1080
window_height = 720
screen_width = game.winfo_screenwidth()
screen_height = game.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
game.geometry(f'{window_width}x{window_height}+{x}+{y}')

pergunta = Label(text='Faça sua escolha:')
pergunta.grid(column=0,pady=10,sticky='w')

pedra = Button(text='Pedra',width = 10)
pedra.grid(pady=10,padx=10,sticky='w')

papel = Button(text='Papel',width = 10)
papel.grid(sticky='w',column=1,pady=0)

tesoura = Button(text='Tesoura',width = 10)
tesoura.grid(column=2,row=0)

paper = PhotoImage(file='C:/Users/patri/Downloads/papel.png')
label_imagem = Label(game, image=paper)
label_imagem.grid(columnspan=6,pady=180,padx=100)

game.mainloop()