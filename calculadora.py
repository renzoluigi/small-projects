from tkinter import *

number = ''

def clean_visor():
    visor_var.set('')
    visor.config(justify='right')

def update_visor():
    visor_var.set(number)
    visor.config(justify='right')

def press1():
    global number
    number += '1'
    update_visor()


def press2():
    global number
    number += '2'
    update_visor()


def press3():
    global number
    number += '3'
    update_visor()


def press4():
    global number
    number += '4'
    update_visor()


def press5():
    global number
    number += '5'
    update_visor()


def press6():
    global number
    number += '6'
    update_visor()


def press7():
    global number
    number += '7'
    update_visor()


def press8():
    global number
    number += '8'
    update_visor()


def press9():
    global number
    number += '9'
    update_visor()


def press0():
    global number
    number += '0'
    update_visor()


def erase():
    global number
    number = number[:-1]
    update_visor()


def operator_plus():
    global number
    if len(number) > 0:
        if number[-1] in '÷%+-×':
            number = number[:-1] + '+'
        else:
            number += '+'
    update_visor()


def operator_minus():
    global number
    if len(number) > 0:
        if number[-1] in '÷%+-×':
            number = number[:-1] + '-'
        else:
            number += '-'
    update_visor()


def operator_multiplication():
    global number
    if len(number) > 0:
        if number[-1] in '÷%+-×':
            number = number[:-1] + '×'
        else:
            number += '×'
    update_visor()


def operator_division():
    global number
    if len(number) > 0:
        if number[-1] in '÷%+-×':
            number = number[:-1] + '÷'
        else:
            number += '÷'
    update_visor()


def operator_rest():
    global number
    if len(number) > 0:
        if number[-1] in '÷%+-×':
            number = number[:-1] + '%'
        else:
            number += '%'
    update_visor()


def result():
    global number
    if len(number) > 0:
        number = number.replace('÷','/')
        number = number.replace('×','*')
        number = number.replace(',','.')
        number = str(eval(number))
        number = number.replace('.', ',')
    update_visor()


def secrecy():
    visor_var.set('NADA MESMO!')
    visor.config(justify='center')
    window.after(3000, lambda: update_visor())

def add_comma():
    global number
    if len(number) > 0:
        if number[-1] == ',':
            number = number[:-1] + ','
        else:
            number += ','
    update_visor()


def erase_all():
    global number
    number = ''
    update_visor()


window = Tk()
window.title('Calculadora')
window.geometry('400x470')

visor_var = StringVar()

visor = Entry(window, font=("Arial", 30), bd=10, state="readonly", width=16, textvariable=visor_var, justify='right')
visor.grid(row=0, column=0, columnspan=3, padx=17, pady=20, sticky="w")

delete = Button(window, text='<--', width=10, bd=3, height=3,command=erase)
delete.grid(row=2, column=0, padx=17, pady=5, sticky="w")

clear = Button(window, text='C', width=10, bd=3, height=3,command=erase_all)
clear.grid(row=2, column=0, padx=110, pady=5, sticky="w")

rest = Button(window, text='%', width=10, bd=3, height=3,command=operator_rest)
rest.grid(row=2, column=0, padx=205, pady=5, sticky="w")

division = Button(window, text='÷', width=10, bd=3, height=3,command=operator_division)
division.grid(row=2, column=0, padx=300, pady=5, sticky='w')

multiplication = Button(window, text='×', width=10, bd=3, height=3,command=operator_multiplication)
multiplication.grid(row=3, column=0, padx=300, pady=5, sticky='w')

minus = Button(window, text='–', width=10, bd=3, height=3,command=operator_minus)
minus.grid(row=4, column=0, padx=300, pady=5, sticky='w')

plus = Button(window, text='+', width=10, bd=3, height=3,command=operator_plus)
plus.grid(row=5, column=0, padx=300, pady=5, sticky='w')

seven = Button(window, text='7', width=10, bd=3, height=3, command=press7)
seven.grid(row=3, padx=17, pady=5, sticky="w")

eight = Button(window, text='8', width=10, bd=3, height=3, command=press8)
eight.grid(row=3, column=0, padx=110, pady=5, sticky="w")

nine = Button(window, text='9', width=10, bd=3, height=3, command=press9)
nine.grid(row=3, column=0, padx=205, pady=5, sticky="w")

four = Button(window, text='4', width=10, bd=3, height=3, command=press4)
four.grid(row=4, padx=17, pady=5, sticky="w")

five = Button(window, text='5', width=10, bd=3, height=3, command=press5)
five.grid(row=4, column=0, padx=110, pady=5, sticky="w")

six = Button(window, text='6', width=10, bd=3, height=3, command=press6)
six.grid(row=4, column=0, padx=205, pady=5, sticky="w")

one = Button(window, text='1', width=10, bd=3, height=3, command=press1)
one.grid(row=5, padx=17, pady=5, sticky="w")

two = Button(window, text='2', width=10, bd=3, height=3, command=press2)
two.grid(row=5, column=0, padx=110, pady=5, sticky="w")

three = Button(window, text='3', width=10, bd=3, height=3, command=press3)
three.grid(row=5, column=0, padx=205, pady=5, sticky="w")

secret = Button(window, text='NADA', width=10, bd=3, height=3,command=secrecy)
secret.grid(row=6, column=0, padx=17, pady=5, sticky="w")

zero = Button(window, text='0', width=10, bd=3, height=3, command=press0)
zero.grid(row=6, column=0, padx=110, pady=5, sticky="w")

comma = Button(window, text=',', width=10, bd=3, height=3,command=add_comma)
comma.grid(row=6, column=0, padx=205, pady=5, sticky="w")

equal = Button(window, text='=', width=10, bd=3, height=3,command=result)
equal.grid(row=6, column=0, padx=300, pady=5, sticky='w')

window.mainloop()
