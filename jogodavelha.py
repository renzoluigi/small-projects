from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Jogo da Velha')
window.geometry('555x480')
X_turn = True


def switch_turn():
    global X_turn
    X_turn = not X_turn


def restart_game():
    for button in buttons:
        button['text'] = ''


def check_winner():
    if pos1['text'] == pos2['text'] == pos3['text']: #linha lateral esquerda
        return pos1['text']
    if pos1['text'] == pos4['text'] == pos7['text']: #linha superior
        return pos1['text']
    if pos4['text'] == pos5['text'] == pos6['text']: #linha do meio
        return pos4['text']
    if pos2['text'] == pos5['text'] == pos8['text']: #linha central
        return pos2['text']
    if pos7['text'] == pos8['text'] == pos9['text']: #linha lateral direita
        return pos7['text']
    if pos3['text'] == pos6['text'] == pos9['text']: #linha inferior
        return pos3['text']
    if pos1['text'] == pos5['text'] == pos9['text']: #diagonal 1
        return pos1['text']
    if pos3['text'] == pos5['text'] == pos7['text']: #diagonal 2
        return pos3['text']
    return None


def mark(pos):
    if pos['text'] == '':
        pos['text'] = 'X' if X_turn else 'O'
        switch_turn()
        winner = check_winner()
        if winner:
            messagebox.showinfo("Fim de Jogo", f"O jogador {winner} venceu!")
            restart_game()
        elif all(button['text'] != '' for button in buttons):
            messagebox.showinfo('Fim de jogo','Empate')
            restart_game()
    else:
        messagebox.showinfo('ERRO!', 'Essa posição ja foi preenchida.')


#9 botoes, turno false e turno true alternando entre X e O, se x[0[ == x[1] bla bla bla, fazer um definidor de turno, mostrar um alerta apos ser declarado o vencedor, te rum selecionador de x/o
pos1 = Button(height=10,width=25,bd=2,command=lambda: mark(pos1))
pos1.grid()
pos2 = Button(height=10,width=25,bd=2,command=lambda: mark(pos2))
pos2.grid()
pos3 = Button(height=10,width=25,bd=2,command=lambda: mark(pos3))
pos3.grid()
pos4 = Button(height=10,width=25,bd=2,command=lambda: mark(pos4))
pos4.grid(column=1,row=0)
pos5 = Button(height=10,width=25,bd=2,command=lambda: mark(pos5))
pos5.grid(column=1,row=1)
pos6 = Button(height=10,width=25,bd=2,command=lambda: mark(pos6))
pos6.grid(column=1,row=2)
pos7 = Button(height=10,width=25,bd=2,command=lambda: mark(pos7))
pos7.grid(column=2,row=0)
pos8 = Button(height=10,width=25,bd=2,command=lambda: mark(pos8))
pos8.grid(column=2,row=1)
pos9 = Button(height=10,width=25,bd=2,command=lambda: mark(pos9))
pos9.grid(column=2,row=2)
buttons = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9]
window.mainloop()
