"""Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной
реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую
графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка."""

from random import choice, randrange
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


def product(*args, repeat=1):
    # если нет аргументов, возвращаем пустой список
    pools = list(map(tuple, args)) * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


class buying_laptops:
    def __init__(self, main):
        s = ttk.Style()
        s.configure('my.TButton', font='Arial 16')

        self.first_click = True

        self.main = main
        self.main_label = Label(main, text='Если хотите получить выборку всевозможных покупок:', font='Arial 16')
        self.label1 = Label(text='\nВведите кол-во покупаемых компьютеров:', font='Arial 16')
        self.entry1 = ttk.Entry(width=30, justify='center', font='Arial 16')

        self.label2 = ttk.Label(text='Введите кол-во типов компьютеров:', font='Arial 16')
        self.entry2 = ttk.Entry(width=30, justify='center', font='Arial 16')

        self.main_button = ttk.Button(text='Рассчитать', command=self.result, style='my.TButton')

        self.main_label.place(x=100,y=10)
        self.label1.place(x=157,y=40)
        self.entry1.place(x=177,y=100)
        self.label2.place(x=177,y=140)
        self.entry2.place(x=177,y=170)
        self.main_button.place(x=280,y=250)

    def result(self):
        self.combr = []
        self.maxstr = []
        self.purchases = []
        self.combinations = []
        self.maxs = self.cntcomps = self.cnttips = 0
        self.BRANDS = ['Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'Acer', 'MSI', 'Samsung']

        try:
            self.conditions = True
            self.cntcomps = int(self.entry1.get())
            self.cnttips = int(self.entry2.get())

            if (self.cntcomps > 4 and self.cnttips > 10) or self.cntcomps > 6 or self.cnttips > 12:
                messagebox.showwarning(title='Ошибка', message='Вы ввели слишком большие числа.')
                self.conditions = False

            if self.cntcomps < 1 or self.cnttips < 1:
                messagebox.showwarning(title='Ошибка', message='Принимаются только положительные числа.')
                self.conditions = False

            if self.conditions:
                self.calculations()

                if self.first_click:
                    self.result_window()
                    self.first_click = False
                else:
                    self.purchases_window.destroy()
                    self.result_window()

        except ValueError:
            messagebox.showwarning(title='Ошибка', message='Введено не число.')

    def calculations(self):
        self.computers = [f'№ {i}: {choice(self.BRANDS)}' for i in range(1, self.cnttips + 1)]

        self.сomp1 = str(self.computers)[2:-1].replace("'", '')

        if self.computers:
            self.comp2 = str(self.computers)[2:-1].replace("'", '')
        else:
            messagebox.showwarning(title='Жаль', message='Сегодня мы осталисть без покупок.')

        for i, varu in enumerate(product(self.computers, repeat=self.cntcomps)):
            s = 0
            b = {}

            for j in sorted(varu):
                if j in b:
                    b[j] = b[j] + 1
                else:
                    b[j] = 1

            if b not in self.combr:
                self.combinations.append(varu)

            self.combr.append(b)

        self.purchases = []
        for i, varu in enumerate(sorted(self.combinations, key=len)):
            self.h = str(varu)[1:-2].replace("'", '').replace(', ', ' | ')
            self.purchases.append(f'{i + 1}. {self.h}')

    def result_window(self):
        self.purchases_window = Toplevel()
        self.purchases_window.title('Список покупок')
        self.purchases_window.geometry('720x480')

        self.purchases_list = Listbox(self.purchases_window)
        self.purchases_list.pack(side='left', fill='both', expand=1)

        for i in self.purchases:
            self.purchases_list.insert('end', i)

        self.scrollbar = Scrollbar(self.purchases_window, command=self.purchases_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.purchases_list.config(yscrollcommand=self.scrollbar.set)


root = Tk()
root.title('Лабораторная № 8')
root.geometry('720x320')
root.resizable(False, False)

buying_laptops(root)

root.mainloop()
