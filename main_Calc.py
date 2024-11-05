from email.policy import default
from tkinter import *
from tkinter import ttk
import math_operator as ma1


def rezult():
    rez = None
    second_n = float(line_input.get())
    line_input.delete(0, END)
    if operator == "+":
        rez = ma.add(first_n, second_n)
    elif operator == "-":
        rez = ma.subtract(first_n, second_n)
    elif operator == "*":
        rez = ma.multiply(first_n, second_n)
    elif operator == "/":
        rez = ma.devide(first_n, second_n)
    line_input.insert(0, rez)


def choise_n(num):
    line_input.insert(END, num)


def choice_o(oper):
    global operator, first_n
    first_n = float(line_input.get())
    operator = oper
    line_input.delete(0, END)


def clear_line():
    line_input.delete(0, END)


first_n = None
operator = None



window = Tk()
window.title("Калькулятор_Стар")
window.iconbitmap(default="Calculator.ico")
line_input = Entry(window, font=("Arial", 14))
line_input.grid(row=0, column=0, columnspan=4, sticky="ew")

ttk.Button(window, text="7", command=lambda : choise_n("7")).grid(row=1, column=0)
ttk.Button(window, text="8", command=lambda : choise_n("8")).grid(row=1, column=1)
ttk.Button(window, text="9", command=lambda : choise_n("9")).grid(row=1, column=2)
ttk.Button(window, text="4", command=lambda : choise_n("4")).grid(row=2, column=0)
ttk.Button(window, text="5", command=lambda : choise_n("5")).grid(row=2, column=1)
ttk.Button(window, text="6", command=lambda : choise_n("6")).grid(row=2, column=2)
ttk.Button(window, text="1", command=lambda : choise_n("1")).grid(row=3, column=0)
ttk.Button(window, text="2", command=lambda : choise_n("2")).grid(row=3, column=1)
ttk.Button(window, text="3", command=lambda : choise_n("3")).grid(row=3, column=2)
ttk.Button(window, text="0", command=lambda : choise_n("0")).grid(row=4, column=0)

ttk.Button(window, text="+", command=lambda: choice_o("+")).grid(row=1, column=3)
ttk.Button(window, text="-", command=lambda: choice_o("-")).grid(row=2, column=3)
ttk.Button(window, text="*", command=lambda: choice_o("*")).grid(row=3, column=3)
ttk.Button(window, text="/", command=lambda: choice_o("/")).grid(row=4, column=3)
ttk.Button(window, text="C", command=lambda: clear_line).grid(row=4, column=1)
ttk.Button(window, text="=", command=lambda: rezult).grid(row=4, column=2)




window.mainloop()